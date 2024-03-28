from flet import *
from task_checkbox import CustomCheckBox

def main(page: Page):
    BG = '#041955'
    FWG = '#97B4FF'
    FG = '#3450A1'
    PINK = '#EB06FF'

    circle = Stack(
     controls=[
      Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
      Container(
                  gradient=SweepGradient(
                      center=alignment.center,
                      start_angle=0.0,
                      end_angle=3,
                      stops=[0.5,0.5],
                  colors=['#00000000', PINK],
                  ),
                  width=100,
                  height=100,
                  border_radius=50,
                  content=Row(alignment='center',
                      controls=[
                        Container(padding=padding.all(5),
                          bgcolor=BG,
                          width=90,height=90,
                          border_radius=50,
                          content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                          content=CircleAvatar(opacity=0.8,
                foreground_image_url="https://www.shutterstock.com/image-vector/default-avatar-profile-icon-social-600nw-1677509740.jpg"
            )
                          )
                          )
                      ],
                  ),
              ),
      
    ]
  )
    


    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius=border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()


    create_task_view = Container(
        content= Container(on_click=lambda _: page.go('/'),
            height=50,
            width=50,
            content=Text('X')
        )
    )

    # tasks = ["Grocery shopping", "Morning workout", "Doctor's appointment", "Finish book", "Organize workspace", "Write journal", "Meal prep", "Practice new skill/hobby"]
    # tasks_card = Column(
    #     height=375,
    #     scroll='auto',
    # )

    # for index, task in enumerate(tasks):
    #     tasks_card.controls.append(
    #         Container(height=70,
    #                   width=400,
    #                   bgcolor=BG,
    #                   border_radius=35,
    #                   padding=padding.only(
    #                     left=20,
    #                     top=23
    #                   ),
    #                   content=CustomCheckBox(
    #                     color=PINK,
    #                     label=task,
    #                     label_color='white'
    #                     ))
    #     )

    tasks = Column(
        height=375,
        scroll='auto',
    )

    task_list = ["Grocery shopping", "Morning workout", "Doctor's appointment", "Finish book", "Organize workspace", "Write journal", "Meal prep", "Practice new skill/hobby"]

    
    for task_label in task_list:
        task_checkbox = CustomCheckBox(
            color=PINK,
            label=task_label,
            label_color='white'
        )
        tasks.controls.append(
            Container(height=70,
                      width=400,
                      bgcolor=BG,
                      border_radius=35,
                      padding=padding.only(
                        left=20,
                        top=23
                      ),
                      content=task_checkbox
        ))
    
    categories_card = Row(
        scroll='auto'
    )
    categories = ['Friends', 'Family', 'Business' ]
    for index, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                bgcolor=BG,
                height=110,
                width=170,
                padding=15,
                border_radius=20,
                content=Column(
                    controls=[
                        Text(str(index + 5) + ' Tasks',
                             color='white'),
                        Text(category,
                             color='white'),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=index * 30),
                            content=Container(bgcolor=PINK) 
                        )
                    ]
                )
            )
        )
    
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            on_click=lambda e: shrink(e),
                            content=Icon(
                                icons.MENU,
                                color='white')),
                        Row(
                            controls=[
                                Icon(icons.SEARCH,
                                    color='white'),
                                Icon(icons.NOTIFICATIONS_OUTLINED,
                                    color='white')])

                    ]
                ),
                Container(height=20),
                Text(
                    value='Personal Task-tracker',
                    size=23,
                    color='white'
                ),
                Text(
                    value='CATEGORIES',
                    color='#a3a3a3'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),
                Container(height=20),
                Text(
                    value="TODAY'S TASKS",
                    color='white'
                ),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2, right=20,
                            icon = icons.ADD, on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ]
        )
    )

    page_1 = Container(
        width=400,
        height=800,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),

        content=Column(
            controls=[
                Row(alignment='end',
                    controls=[
                        Container(
                            border_radius=25,
                            padding=padding.only(
                            top=11, left=18
                            ),
                             height=50,
                            width=50,
                            border=border.all(color='white', width=1),
                            on_click=lambda e: restore(e),
                            content=Text(
                            value='<',
                            color='white',
                            size=17)
                )
                    ]
                ),
                Container(height=20),
                circle,
                Text('John Doe', size=32, weight='bold', color='white'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white60'),
                    Text('Templates',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL,color='white60'),
                    Text('Templates',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED,color='white60'),
                    Text('Templates',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),

                Image(src=f"/images/1.png",
                    width=300,
                    height=200,
                ),
                Text('Good',color=FG,font_family='poppins',),
                Text('Consistency',size=12, color=FG)
            ]
        )
    )
    page_2 = Row(
        alignment='end',
        controls=[
            Container(
                width=400,
                height=800,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=400,
        height=800,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/': View(
                "/",
                [
                   container
                ],
             ),
        '/create_task': View(
                            "/create_task",
                            [
                              create_task_view
                            ]
                        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
          pages[page.route]
        )

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
