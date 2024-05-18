import flet as ft



def main(page: ft.Page):

    t = ft.Text(value="Age", color="Black")
    page.controls.append(t)
    page.update()

    def button_clicked(e):
        output_text.value = f"Your age is :  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("22"),
            ft.dropdown.Option("20"),
            ft.dropdown.Option("18"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)

    t = ft.Text(value="Name", color="Black")
    page.controls.append(t)
    page.update()
    
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
           
            page.add(ft.Text(f"Your name is : {name}"))

    txt_name = ft.TextField(label="Your name")



    page.add(txt_name, ft.ElevatedButton("Submit", on_click=btn_click))


    t = ft.Text(value="Apply", color="Black")
    page.controls.append(t)
    page.update()
    
    
    def button_clicked(e):
        page.add(ft.Text(f"{txt_name.value} and {output_text.value}"))

    page.add(ft.ElevatedButton(text="✔️", on_click=button_clicked))

ft.app(target=main)