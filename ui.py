import flet as ft
import funcs
import datetime

WIDTH = 800 * 9 / 16
HEIGHT = 800 * 16 / 9


def money(page: ft.Page):

    depositInput = ft.TextField(label="Cantidad a Depositar/Retirar")

    purposeInput = ft.TextField(label="Motivo de Retiro")
    balanceText = ft.Text(
        value=f"Saldo:{funcs.GetBalance()}",
        size=20,
        text_align=ft.TextAlign.CENTER,
        width=WIDTH,
    )

    def onDepositClick(e):
        valueToDeposit = int(depositInput.value)
        funcs.deposit(valueToDeposit, datetime.date.today())
        balanceText.value = f"Saldo:{funcs.GetBalance()}"
        update_operations()
        page.update()

    def onWithdrawClick(e):
        valueToWidthdraw = int(depositInput.value)
        purpose = purposeInput.value
        funcs.withdraw(valueToWidthdraw, purpose, datetime.date.today())
        balanceText.value = f"Saldo:{funcs.GetBalance()}"
        update_operations()
        page.update()

    depositBtn = ft.ElevatedButton(text="Depositar", on_click=onDepositClick)

    withdrawBtn = ft.ElevatedButton(text="Retirar", on_click=onWithdrawClick)

    balance = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    balanceText,
                    depositInput,
                    purposeInput,
                    ft.Row(
                        controls=[
                            depositBtn,
                            withdrawBtn,
                        ],
                        width=WIDTH,
                    ),
                ],
                width=WIDTH,
            ),
            width=WIDTH,
        )
    )

    operations = ft.Column(
        controls=[ft.Text(value=f"{op}") for op in funcs.operations],
        height=HEIGHT / 4,
        scroll=ft.ScrollMode.AUTO,
    )

    def update_operations():
        operations.controls = [ft.Text(value=f"{op}") for op in funcs.operations][::-1]

    TransactionHistory = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[ft.Text("Historial de Transacciones:"), operations]
            ),
            padding=10,
            width=WIDTH,
        )
    )

    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.add(balance, TransactionHistory)


def tasks(page: ft.Page):

    currentClass = funcs.GetCurrentClass()

    Nombre = currentClass["Nombre"]
    HoraInicio = currentClass["HoraInicio"]
    HoraFin = currentClass["HoraFin"]
    Salon = currentClass["Salon"]

    tareas = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value=f"Nombre : {Nombre}"),
                    ft.Text(value=f"Hora: {HoraInicio} -> {HoraFin}"),
                    ft.Text(value=f"Salon: {Salon}"),
                ],
                width=WIDTH,
            ),
            width=WIDTH,
            padding=10,
        ),
        width=WIDTH,
    )

    taskNameInput = ft.TextField(label="Nombre de la tarea")

    taskDate = None

    def changeDate(e):
        global taskDate
        taskDate = taskDatePicker.value

    taskDatePicker = ft.DatePicker(on_change=changeDate)

    def openDatePicker(e):

        taskDatePicker.pick_date()

    def makeTask(e):
        global taskDate
        t = funcs.Task(taskNameInput.value, "", taskDate.date())
        update_tareas()
        page.update()

    tareasP = ft.Column(controls=[ft.Text(value=f"{op}") for op in funcs.tasks])

    TareasPendientes = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[ft.Text("Historial de Transacciones:"), tareasP]
            ),
            padding=10,
            width=WIDTH,
        )
    )

    def update_tareas():
        tareasP.controls = [ft.Text(value=f"{op}") for op in funcs.tasks]

    pendientes = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="Tareas Pendientes:"),
                    taskNameInput,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Agregar Tarea", on_click=makeTask),
                            ft.ElevatedButton(
                                text="Seleccionar Fecha", on_click=openDatePicker
                            ),
                        ]
                    ),
                ],
                width=WIDTH,
            ),
            width=WIDTH,
            padding=10,
        ),
        width=WIDTH,
    )

    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.add(tareas, pendientes, taskDatePicker, TareasPendientes)


ft.app(target=tasks)
