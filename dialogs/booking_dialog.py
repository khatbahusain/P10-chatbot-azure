# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Flight booking dialog."""

from datatypes_date_time.timex import Timex

from botbuilder.dialogs import WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.dialogs.prompts import ConfirmPrompt, TextPrompt, PromptOptions
from botbuilder.core import MessageFactory, BotTelemetryClient, NullTelemetryClient
from .cancel_and_help_dialog import CancelAndHelpDialog
from .date_resolver_dialog import DateResolverDialog


class BookingDialog(CancelAndHelpDialog):
    """Flight booking implementation."""

    def __init__(
        self,
        dialog_id: str = None,
        telemetry_client: BotTelemetryClient = NullTelemetryClient(),
    ):
        super(BookingDialog, self).__init__(
            dialog_id or BookingDialog.__name__, telemetry_client
        )
        self.telemetry_client = telemetry_client
        text_prompt = TextPrompt(TextPrompt.__name__)
        text_prompt.telemetry_client = telemetry_client

        waterfall_dialog = WaterfallDialog(
            WaterfallDialog.__name__,
            [
                self.destination_step,
                self.origin_step,
                self.start_date_step,
                self.end_date_step,
                self.budget_step,
                self.confirm_step,
                self.final_step
            ],
        )
        waterfall_dialog.telemetry_client = telemetry_client

        self.add_dialog(text_prompt)
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))
        self.add_dialog(waterfall_dialog)

        self.initial_dialog_id = WaterfallDialog.__name__

    async def destination_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """Prompt for destination."""
        booking_details = step_context.options

        if booking_details.dst_city is None:
            return await step_context.prompt(
                TextPrompt.__name__,
                PromptOptions(
                    prompt=MessageFactory.text("Could you kindly verify the city to which you would like to travel?")
                ),
            )  # pylint: disable=line-too-long,bad-continuation

        return await step_context.next(booking_details.dst_city)

    async def origin_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """Prompt for origin city."""
        booking_details = step_context.options

        # Capture the response to the previous step's prompt
        booking_details.dst_city = step_context.result
        if booking_details.or_city is None:
            return await step_context.prompt(
                TextPrompt.__name__,
                PromptOptions(
                    prompt=MessageFactory.text("Could you kindly confirm the city from which you will be traveling?")
                ),
            )  # pylint: disable=line-too-long,bad-continuation

        return await step_context.next(booking_details.or_city)

    async def start_date_step(
            self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """Prompt for start travel date"""

        booking_details = step_context.options

        # Capture the results of the previous step
        booking_details.or_city = step_context.result
        if booking_details.str_date is None:
            return await step_context.prompt(
                TextPrompt.__name__,
                PromptOptions(
                    prompt=MessageFactory.text("Could you kindly confirm when you wish to begin your travel?")
                ),
            )  # pylint: disable=line-too-long

        return await step_context.next(booking_details.str_date)

    async def end_date_step(
            self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """Prompt for end travel date"""

        booking_details = step_context.options

        # Capture the results of the previous step
        booking_details.str_date = step_context.result
        if booking_details.end_date is None:
            return await step_context.prompt(
                TextPrompt.__name__,
                PromptOptions(
                    prompt=MessageFactory.text("Could you kindly confirm when you wish to return?")
                ),
            )  # pylint: disable=line-too-long

        return await step_context.next(booking_details.end_date)

    async def budget_step(
            self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """Prompt for end budget"""

        booking_details = step_context.options

        # Capture the results of the previous step
        booking_details.end_date = step_context.result
        if booking_details.budget is None:
            return await step_context.prompt(
                TextPrompt.__name__,
                PromptOptions(
                    prompt=MessageFactory.text("Could you kindly confirm your budget for this trip?")
                ),
            )  # pylint: disable=line-too-long

        return await step_context.next(booking_details.budget)

    async def confirm_step(
            self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """Confirm the information the user has provided."""
        booking_details = step_context.options

        # Capture the results of the previous step
        booking_details.budget = step_context.result
        msg = (
            f"You would like to travel to: {booking_details.dst_city}"
            f" from: {booking_details.or_city} departing: {booking_details.str_date}, returing "
            f"{booking_details.end_date}, with a budget of {booking_details.budget} "
        )
        
        return await step_context.prompt(
                TextPrompt.__name__,
                PromptOptions(
                    prompt=MessageFactory.text(msg)
                ),
            )


    async def final_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:

        return await step_context.end_dialog()

    def is_ambiguous(self, timex: str) -> bool:
        """Ensure time is correct."""
        timex_property = Timex(timex)
        return "definite" not in timex_property.types

##