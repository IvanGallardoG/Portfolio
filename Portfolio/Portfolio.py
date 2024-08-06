import reflex as rx
import asyncio
from rxconfig import config

color_scheme = {

    "accordion": "#222",  # Color de fondo
}

class verModal(rx.State):
    visible = False
    valor : str = None

    def change(self):
        self.visible = not (self.visible)

    def val(self, val):
        self.valor = val
    
    def borrar(self):
        self.valor = None


class Refrescar(rx.State):
    refresh: int = 0

    def refresh_icons(self):
        for i in range(100):
            self.refresh += 1
            yield

class ButtonState(rx.State):
    active_button: int = 1

    def set_active_button(self, button_id: int):
        self.active_button = button_id

    @staticmethod
    def button_color(id: int) -> str:
        return "gold" if ButtonState.active_button == id else "white"

def tarjeta() -> rx.Component:
    return rx.vstack(
            rx.avatar(src="ivan.webp", fallback="IG", size="8", alt="Imagen del creador del sitio"),
            rx.heading("Iván Gallardo", size="8"),
            rx.badge("Software Developer", radius="large", variant="soft", color_scheme="gray", size="10", padding="5px 10px", font_weigh="bold"),
            rx.divider(
                    size="4",
                    width="80%",
                    ),
            rx.flex(
                rx.flex(
                    rx.card(
                        rx.icon(tag="mail", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("EMAIL", size="1", font_weight="300"),
                        rx.heading("ivangallardog@icloud.com", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="smartphone", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("PHONE", size="1", font_weight="300"),
                        rx.heading("+52 4921076419", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="map-pin", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("LOCATION", size="1", font_weight="300"),
                        rx.heading("GUADALAJARA, MEXICO", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="calendar-days", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("BIRTHDAY", size="1", font_weight="300"),
                        rx.heading("JUNE 15, 1999", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                spacing="5",
                direction="column",
                align="start",
                padding="0 10px 0 20px",
            ),
            rx.flex(
                rx.link(rx.icon(tag="linkedin", color="white", size=20, _hover={"color":"gold"}), href="https://www.linkedin.com/in/ivangallardog", is_external=True),
                rx.link(rx.icon(tag="github", color="white", size=20, _hover={"color":"gold"}), href="https://github.com/IvanGallardoG", is_external=True),
                rx.link(rx.icon(tag="instagram", color="white", size=20, _hover={"color":"gold"}), href="https://www.instagram.com/ivangallardog", is_external=True),
                direction="row",
                spacing="5",
            ),
            spacing="5",
            justify="center",
            align="center",
            height="620px",
            width="280px",
            background_color="#222",
            border_radius="30px",
        )

def tarjeta_tablet() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.avatar(src="ivan.webp", fallback="IG", size="8"),
            rx.heading("Iván Gallardo", size="8"),
            rx.badge("Software Developer", radius="large", variant="soft", color_scheme="gray", size="10", padding="5px 10px", font_weigh="bold"),
            rx.flex(
                rx.link(rx.icon(tag="linkedin", color="white", size=20, _hover={"color":"gold"}), href="https://www.linkedin.com/in/ivangallardog/", is_external=True),
                rx.link(rx.icon(tag="github", color="white", size=20, _hover={"color":"gold"}), href="https://github.com/IvanGallardoG", is_external=True),
                rx.link(rx.icon(tag="instagram", color="white", size=20, _hover={"color":"gold"}), href="https://www.instagram.com/ivangallardog/", is_external=True),
                direction="row",
                spacing="5",
                width="100%",
                align="center",
                justify="center",
            ),
            direction="column",
            align="center",
            justify="between",
            text_align="center",
            spacing="3",
        ),
            rx.flex(
                rx.flex(
                    rx.card(
                        rx.icon(tag="mail", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("EMAIL", size="1", font_weight="300"),
                        rx.heading("ivangallardog@icloud.com", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="smartphone", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("PHONE", size="1", font_weight="300"),
                        rx.heading("+52 4921076419", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="map-pin", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("LOCATION", size="1", font_weight="300"),
                        rx.heading("GUADALAJARA, MEXICO", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="calendar-days", color="gold", width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_iterms="center",
                    ),
                    rx.flex(
                        rx.heading("BIRTHDAY", size="1", font_weight="300"),
                        rx.heading("JUNE 15, 1999", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                spacing="6",
                direction="column",
                align="baseline",
            ),
            gap="50px",
            justify="center",
            align="center",
            min_height="5vh",
            width="85vw",
            background_color="#222",
            border_radius="30px",
            direction="row",
            padding="30px",
        )

class AccordionState(rx.State):
    expanded: bool = False

    def toggle(self):
        self.expanded = not self.expanded

def tarjeta_mobile():
    return rx.accordion.root(
        rx.accordion.item(
            header=rx.vstack(
            rx.avatar(src="ivan.webp", fallback="IG", size="8"),
            rx.heading("Iván Gallardo", size="8"),
            rx.badge("Software Developer", radius="large", variant="soft", color_scheme="gray", size="10", padding="5px 10px", font_weigh="bold"),
            align="center",
            justifu="center",
            width="100%",
            height="100%",
            ),
            content=rx.vstack(
            rx.divider(
                size="4",
                width="80%",
                ),
            rx.flex(
                rx.flex(
                    rx.card(
                        rx.icon(tag="mail", color="gold", display="block", key=Refrescar.refresh, width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_items="center",
                    ),
                    rx.flex(
                        rx.heading("EMAIL", size="1", font_weight="300"),
                        rx.heading("ivangallardog@icloud.com", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="smartphone", color="gold", display="block",key=Refrescar.refresh, width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_items="center",
                    ),
                    rx.flex(
                        rx.heading("PHONE", size="1", font_weight="300"),
                        rx.heading("+52 4921076419", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="map-pin", color="gold", display="block", key=Refrescar.refresh, width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_items="center",
                    ),
                    rx.flex(
                        rx.heading("LOCATION", size="1", font_weight="300"),
                        rx.heading("GUADALAJARA, MEXICO", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                rx.flex(
                    rx.card(
                        rx.icon(tag="calendar-days", color="gold", display="block", key=Refrescar.refresh, width="100%", height="100%"),
                        width="40px",
                        height="40px",
                        align_items="center",
                    ),
                    rx.flex(
                        rx.heading("BIRTHDAY", size="1", font_weight="300"),
                        rx.heading("JUNE 15, 1999", size="2", font_weight="500", color="white"),
                        direction="column",
                        justify="center",
                    ),
                    gap="10px",
                    direction="row",
                    justify="center",
                    align="center",
                ),
                spacing="5",
                direction="column",
                align="start",
                padding="0 10px 0 20px",
            ),
            rx.divider(
                size="4",
                width="80%",
                ),
            rx.flex(
                rx.link(rx.icon(tag="linkedin", color="white", size=20, _hover={"color":"gold"}), href="https://www.linkedin.com/in/ivangallardog/", is_external=True),
                rx.link(rx.icon(tag="github", color="white", size=20, _hover={"color":"gold"}), href="https://github.com/IvanGallardoG", is_external=True),
                rx.link(rx.icon(tag="instagram", color="white", size=20, _hover={"color":"gold"}), href="https://www.instagram.com/ivangallardog/", is_external=True),
                direction="row",
                spacing="5",
            ),
            align="center",
            justifu="center",
            width="100%",
            height="100%",
            ),
            background_color="#222",
            on_click=Refrescar.refresh_icons,
        ),
        collapsible=True,
        width="85vw",
        min_height="5vh",
        background_color="#222",
        color_scheme="gray",
        variant="soft",
        style={"z_index":"10"},
    )


def barra() -> rx.Component:
    return rx.flex(
        button_desk(1, "About"),
        button_desk(2, "Resume"),
        button_desk(3, "Portfolio"),
        #button_desk(4, "Blog"),
        button_desk(5, "Contact"),
        direction="row",
        justify="between",
        align="center",
        background_color="#333",
        #width="500px", con 5 opciones
        width="400px", #con 4 opciones
        padding="15px",
        border_radius="0 30px 0 30px",
        position="absolute",
        top="0",
        right="0",
        style={"z_index":"1000"}
    )

def button(id: int, label: str) -> rx.Component:
    return rx.button(
        label,
        background_color="transparent",
        _active={"outline": "none"},
        _hover={"color":"gray"},
        font_size=["0.7rem", "1rem", "1.1rem"], 
        color=rx.cond(ButtonState.active_button == id, "gold", "white"),
        on_click=lambda: ButtonState.set_active_button(id),
    )

def button_mobile(id: int, label: str) -> rx.Component:
    return rx.button(
        label,
        background_color="transparent",
        _active={"outline": "none"},
        _hover={"color":"gray"},
        font_size="2em",  
        color=rx.cond(ButtonState.active_button == id, "gold", "white"),
        on_click=[lambda: ButtonState.set_active_button(id), DrawerState.toggle_drawer],
    )

def button_desk(id: int, label: str) -> rx.Component:
    return rx.button(
        label,
        background_color="transparent",
        _active={"outline": "none"},
        _hover={"color":"gray"},
        font_size="17px", 
        color=rx.cond(ButtonState.active_button == id, "gold", "white"),
        on_click=lambda: ButtonState.set_active_button(id),
    )

def barra_mobile() -> rx.Component:
    return rx.flex(
        button(1, "About"),
        button(2, "Resume"),
        button(3, "Portfolio"),
        #button(4, "Blog"),
        button(5, "Contact"),
        direction="row",
        justify="center",
        align="center",
        background_color="#333",
        width="100vw",
        padding="8px",
        border_radius="30px 30px 0 0",
        position="fixed",
        bottom="0",
        left="0",
        background="#222222ee",
        box_shadow="0 0 6px gold",
        style={"z_index":"1000"},
    )

class DrawerState(rx.State):
    is_open: bool = False

    def toggle_drawer(self):
        self.is_open = not self.is_open

def drawer_mobile() -> rx.Component:
    return rx.drawer.root(
    rx.drawer.trigger(rx.button(rx.icon(tag="menu", size=30, on_click=DrawerState.toggle_drawer), style={"outline": "none", "border":"none"}), position="fixed", top="1em", right="1em", style={"z_index":"10000"}, background_color="transparent"),
    rx.drawer.overlay(z_index="5", on_click=DrawerState.toggle_drawer, style={"outline": "none", "border":"none"}),
    rx.drawer.portal(
        rx.drawer.content(
            rx.flex(
                button_mobile(1, "About"),
                button_mobile(2, "Resume"),
                button_mobile(3, "Portfolio"),
                #button_mobile(4, "Blog"),
                button_mobile(5, "Contact"),
                align_items="center",
                justify="center",
                direction="column",
                gap="3em",
                width="100%",
                style={"outline": "none", "border":"none"},
            ),
            top="auto",
            right="auto",
            height="100%",
            width="80vw",
            background_color="#333333dd",
            style={"outline": "none", "border":"none"},
            # background_color=rx.color("green", 3)
        ),
        style={"outline": "none", "border":"none"},
    ),
    open=DrawerState.is_open,
    direction="left",
    style={"outline": "none", "border":"none"},
)

def about() -> rx.Component:
    return rx.flex(
        rx.heading("About Me", size="8"),
        rx.divider(size="4", width="50px", height="5px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
        rx.text(
            "I'm a Junior Software Developer from Mexico, working in fullstack web and mobile development. I enjoy learning new things everyday and turning complex problems into simple.", size="4",
        ),
        rx.text(
            "I am always looking for opportunities to work on innovative and challenging projects, with the goal of continuously learning and improving as a developer to contribute solutions that make a positive impact. I aim to collaborate on projects with meaningful purposes that enhance people's lives through technology.", size="4",
        ),
        rx.heading("What I'm Doing", size="7"),
        rx.grid(
            rx.card(
                rx.flex(
                    rx.flex(
                        rx.icon(tag="code", color="gold", size=50),
                        rx.heading("Automation", size="6"),
                        rx.text("I develop scripts using Python and Bash to automate repetitive tasks, streamline workflows, and enhance efficiency. By leveraging these tools, I create solutions that speed up processes and reduce manual effort, optimizing productivity and accuracy.", size="4"),
                        direction="column",
                        spacing="3",
                        align="center",
                        text_align="center",
                    ),
                    direction="row",
                    spacing="5",
                    align="center",
                    justify="between",
                ),
                padding="20px",
            ),
            rx.card(
                rx.flex(
                    rx.flex(
                        rx.icon(tag="panels-top-left", color="gold", size=50),
                        rx.heading("Web Development", size="6"),
                        rx.text("I create dynamic, responsive websites with a focus on seamless user experience and robust functionality. Combining front-end and back-end skills, I deliver intuitive and effective web solutions.", size="4"),
                        direction="column",
                        spacing="3",
                        align="center",
                        text_align="center",
                    ),
                    direction="row",
                    spacing="5",
                    align="center",
                    justify="between",
                ),
                padding="20px",
            ),
            rx.card(
                rx.flex(
                    rx.flex(
                        rx.icon(tag="tablet-smartphone", color="gold", size=50),
                        rx.heading("Mobile Development", size="6"),
                        rx.text("I build engaging and high-performance mobile applications for both iOS and Android. Leveraging cross-platform and native technologies, I create seamless user experiences and functional apps that meet diverse needs.", size="4"),
                        direction="column",
                        spacing="3",
                        align="center",
                        text_align="center",
                    ),
                    direction="row",
                    spacing="5",
                    align="center",
                    justify="between",
                ),
                padding="20px",
            ),
            
            columns=rx.breakpoints(xs="1", sm="2", md="2", lg="2"),
            spacing="6",
            width="90%",
            margin="auto",
        ),
        rx.spacer(),
        rx.flex(
            rx.card(
                rx.icon(tag="brain-circuit", color="gold", width="100%", height="100%"),
                width="50px",
                height="50px",
                align_items="center",
            ),
            rx.heading("Hard Skills", size="7"),
            direction="row",
            align="center",
            gap="20px",
        ),
        rx.center(
            rx.card(
                rx.vstack(
                    rx.flex(
                        rx.text(rx.text.strong("Python"), " 80%", colot="white"),
                        rx.divider(size="4", width="80%", height="8px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
                        direction="column",
                        width="100%",
                        spacing="1",
                    ),
                    rx.flex(
                        rx.text(rx.text.strong("Bash"), " 60%", colot="white"),
                        rx.divider(size="4", width="60%", height="8px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
                        direction="column",
                        width="100%",
                        spacing="1",
                    ),
                    rx.flex(
                        rx.text(rx.text.strong("HTML & CSS"), " 70%", colot="white"),
                        rx.divider(size="4", width="70%", height="8px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
                        direction="column",
                        width="100%",
                        spacing="1",
                    ),
                    rx.flex(
                        rx.text(rx.text.strong("C++"), " 60%", colot="white"),
                        rx.divider(size="4", width="60%", height="8px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
                        direction="column",
                        width="100%",
                        spacing="1",
                    ),
                    rx.flex(
                        rx.text(rx.text.strong("Flutter, Kotlin, Swift"), " 40%", colot="white"),
                        rx.divider(size="4", width="40%", height="8px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
                        direction="column",
                        width="100%",
                        spacing="1",
                    ),
                    
                    width="100%",
                    spacing="4",
                    font_size="1.2rem",
                ),
                width="100%",
                padding="30px",
            ),
            width="100%",
        ),
        rx.spacer(),
        rx.flex(
            rx.card(
                rx.icon(tag="brain", color="gold", width="100%", height="100%"),
                width="50px",
                height="50px",
                align_items="center",
            ),
            rx.heading("Soft Skills", size="7"),
            direction="row",
            align="center",
            gap="20px",
        ),
        rx.center(
            rx.card(
                rx.grid(
                    rx.box(rx.heading("Problem Solving", color="gold", size="6"), text_align="center", border_radius="5px", padding="10px", background_color="#44444455"),
                    rx.box(rx.heading("Teamwork", color="gold", size="6"), text_align="center", border_radius="5px", padding="10px", background_color="#44444455"),
                    rx.box(rx.heading("Adaptability", color="gold", size="6"), text_align="center", border_radius="5px", padding="10px", background_color="#44444455"),
                    rx.box(rx.heading("Proactivity", color="gold", size="6"), text_align="center", border_radius="5px", padding="10px", background_color="#44444455"),
                    rx.box(rx.heading("Decision-making", color="gold", size="6"), text_align="center", border_radius="5px", padding="10px", background_color="#44444455"),
                    rx.box(rx.heading("Time Management", color="gold", size="6"), text_align="center", border_radius="5px", padding="10px", background_color="#44444455"),
                    columns=rx.breakpoints(xs="1", sm="2", md="3", lg="3"),
                    spacing="4",
                    width="100%",
                ),
                width="100%",
                padding="30px"
            ),
            width="100%",
        ),
        direction="column",
        spacing="5",
        justify="center",
        align="baseline",
        margin="30px",
    )

def tarjeta_resume(insti :str , fecha : str, descripcion : str) -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.icon(tag="chevrons-right", size=30, color="gold"),
            align="center",
            justify="center",
        ),
        rx.flex(
            rx.heading(insti, size="6"),
            rx.text(fecha, font_size="1rem", color="gold"),
            rx.text(descripcion, font_size="1rem", color="white"),
            justify="center",
            direction="column",
        ),
        direction="row",
        align="start",
        justify="center",
        gap="20px",
        padding_left="20px"
    )

def resume() -> rx.Component:
    return rx.flex(
        rx.heading("Resume", size="8"),
        rx.divider(size="4", width="50px", height="5px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
        rx.flex(
            rx.card(
                rx.icon(tag="book-open", color="gold", width="100%", height="100%"),
                width="50px",
                height="50px",
                align_items="center",
            ),
            rx.heading("Education", size="7"),
            direction="row",
            align="center",
            gap="20px",
        ),
        tarjeta_resume("Instituto Politécnico Nacional", "2017 - 2021", "Mechatronics Engineering"),
        rx.link(rx.button("View Final Project", color_scheme="gold", style={"outline": "none", "border":"none"}), href="https://drive.google.com/file/d/1EYeZTXzU90ggiaDfGiPEGpX6VhZco5xe/view?usp=drive_link", is_external=True, padding_left="70px", style={"outline": "none", "border":"none"}),
        rx.spacer(),
        rx.flex(
            rx.card(
                rx.icon(tag="bot", color="gold", width="100%", height="100%"),
                width="50px",
                height="50px",
                align_items="center",
            ),
            rx.heading("Experience", size="7"),
            direction="row",
            align="center",
            gap="20px",
        ),
        tarjeta_resume("FOXCONN | Test Engineer", "October 2023 - Present", "I handle preventive and corrective maintenance, conduct tests, and manage Linux test environments. I automate tasks with scripts, collaborate with teams, and document procedures for efficiency and reliability."),
        tarjeta_resume("FOXCONN | Program Engineer", "May 2022 - October 2023", "I manage the programming of integrated components for electronic boards, oversee label printing, and maintain printers and automatic programming machines. I handle inventory control for parts, tags, and electronic boards, and implement programs to reduce software loading errors."),
        tarjeta_resume("IPN | Engineer Intern (Control Systems)", "March 2021 - October 2021", "I installed a new hydraulic pump, created wiring diagrams for sensors and actuators, and programmed the PLC using ladder logic."),
        rx.spacer(),
        rx.flex(
            rx.card(
                rx.icon(tag="badge-check", color="gold", width="100%", height="100%"),
                width="50px",
                height="50px",
                align_items="center",
            ),
            rx.heading("Certifications", size="7"),
            direction="row",
            align="center",
            gap="20px",
        ),
        #rx.chakra.box(element="embed", src="python3.pdf", width="700px", height="700px", align="center", on_scroll=None),
        #rx.chakra.box(element="iframe", src="bash.pdf", width="50%", height="90vh"),
        rx.grid(
            modal_certificado("/bash.webp", "Bash"),
            modal_certificado("/python3.webp", "Python 3"),
            modal_certificado("/hackerrank.webp", "Python 3 Hackerrank"),
            modal_certificado("/backend1.webp", "Back-end Meta"),
            modal_certificado("/flutter1.webp", "Flutter 1"),
            modal_certificado("/flutter2.webp", "Flutter 2"),
            columns=rx.breakpoints(xs="1", sm="2", md="2", lg="2"),
            spacing="6",
            width="90%",
            margin="auto",
        ),
        rx.center(rx.link(rx.button("Download CV", color_scheme="gold", style={"outline": "none", "border":"none"}), href="https://drive.usercontent.google.com/download?id=12T-tgLazQbQin80lyuN-XsJnuYUQly7p&export=download&authuser=0&confirm=t&uuid=edcf675b-f818-437c-8f8e-182d94adfa6d&at=APZUnTXrtl_uH4GfdSexzpZloAfy:1722800175218", is_external=False, style={"outline": "none", "border":"none"}), width="100%"),
        direction="column",
        spacing="5",
        justify="center",
        align="baseline",
        margin="30px",
    )

def modal() -> rx.Component:
    return rx.cond(
            verModal.valor,
            rx.flex(
                rx.image(src=verModal.valor, max_height="90%"), 
                on_click=verModal.borrar,
                background_color="#00000033",
                position="fixed",
                top="0%",
                left="0%",
                height="100vh",
                width="100vw",
                align="center",
                justify="center",
                style={"z_index":"10000"},
            ),
    )

def modal_certificado(imagen : str, nombre : str) -> rx.Component:
    return rx.flex(
        rx.hover_card.root(
        rx.hover_card.trigger(
            rx.image(src=imagen, on_click=verModal.val(imagen), _hover={"opacity":"0.8"}),
        ),
        rx.hover_card.content(
            rx.text(nombre),
            side="top",
            align="center",
            ),
        ),
        modal(),
        align="center",
        justify="center",
        min_width="200px",
    )



def portfolio() -> rx.Component:
    return rx.flex(
        rx.heading("Portfolio", size="8"),
        rx.divider(size="4", width="50px", height="5px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),

        direction="column",
        spacing="5",
        justify="center",
        align="baseline",
        margin="30px",
    )

def blog() -> rx.Component:
    return rx.flex(
        rx.heading("Blog", size="8"),
        rx.divider(size="4", width="50px", height="5px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),

        direction="column",
        spacing="5",
        justify="center",
        align="baseline",
        margin="30px",
    )

def enviar():
    return rx.script

class formSubmit(rx.State):
    form_data: dict = {}
    message: str = None
    option: str = None
    link: str = ""

    def genLink(self, form_data: dict):
        self.form_data = form_data
        self.form_data["message"]=self.message
        self.form_data["option"]=self.option
        self.link = "https://wa.me/524921076419?text=Hi, my name is "
        self.link = self.link + self.form_data["first_name"] + " " + self.form_data["last_name"] + "%0A"
        self.link = self.link + "I'm interested in " + self.form_data["option"] + "%0A"
        self.link = self.link + self.form_data["message"]+"%0A"
        self.link = self.link + self.form_data["email"] + "%0A"
        self.link = self.link + self.form_data["phone"] + ""
        self.link = self.link.replace(" ","+")
        return rx.redirect(self.link, external=True)
    

def contact() -> rx.Component:
    return rx.flex(
        rx.heading("Contact", size="8"),
        rx.divider(size="4", width="50px", height="5px", border_radius="5px", background="linear-gradient(to right, gold, orange)"),
        rx.spacer(),
        rx.center(
            rx.form(
                rx.vstack(
                    rx.chakra.input(
                        placeholder="First Name",
                        name="first_name",
                        is_required=True,
                        focus_border_color="gold",
                    ),
                    rx.chakra.input(
                        placeholder="Last Name",
                        name="last_name",
                        is_required=True,
                        focus_border_color="gold",
                    ),
                    rx.chakra.input(
                        placeholder="Email",
                        name="email",
                        is_required=True,
                        focus_border_color="gold",
                        type_="email",
                    ),
                    rx.chakra.input(
                        placeholder="Phone",
                        name="phone",
                        is_required=True,
                        focus_border_color="gold",
                        type_="tel",
                    ),
                    rx.chakra.select(
                        ["Automation", "Web Development", "Mobile Applications", "Other"],
                        placeholder="Service",
                        label="Service",
                        is_required=True,
                        focus_border_color="gold",
                        on_change=formSubmit.set_option,
                    ),
                    rx.chakra.text_area(
                        placeholder="Write your message here...",
                        focus_border_color="gold",
                        min_height="250px",
                        is_required=True,
                        on_change=formSubmit.set_message
                    ),
                    rx.center(rx.button("Submit", type="submit", color_scheme="gold", style={"outline": "none"}), width="100%"),
                    ),
                    on_submit=formSubmit.genLink,
                    reset_on_submit=True,
                    width="95%",
            ),
            width="100%",
        ),
        direction="column",
        spacing="5",
        justify="center",
        align="baseline",
        margin="30px",
    )


def index() -> rx.Component:
    return rx.flex(
        rx.desktop_only(
            rx.flex(
                rx.flex(
                    tarjeta(),
                    width="280px",
                    min_height="90vh",
                    align="start",
                    justify="center",
                ),
            rx.flex(
                rx.box(
                    barra(),
                    rx.match(
                        ButtonState.active_button,
                        (1, about()),
                        (2, resume()),
                        (3, portfolio()),
                        (4, blog()),
                        (5, contact()),
                    ),
                    width="100%",
                    background_color="#222",
                    border_radius="30px",
                    position="relative",
                ),
                align="center",
                justify="center",
                style={"width":"calc(75vw)"},
                max_width="2000px",
            ),
            direction="row",
            align="start",
            justify="center",
            gap="30px",
            ),
            margin="30px",
        ),

        rx.tablet_only(
            rx.flex(
                tarjeta_tablet(),
                rx.box(
                    barra(),
                    rx.match(
                        ButtonState.active_button,
                        (1, about()),
                        (2, resume()),
                        (3, portfolio()),
                        (4, blog()),
                        (5, contact()),
                    ),
                    width="95vw",
                    background_color="#222",
                    border_radius="30px",
                    position="relative",
                ),
                direction="column",
                spacing="2",
                align="center",
                justify="center",
            ),
            #barra_mobile(),
            margin="30px",
        ),
        rx.mobile_only(
            rx.flex(
                tarjeta_mobile(),
                rx.box(
                    rx.match(
                        ButtonState.active_button,
                        (1, about()),
                        (2, resume()),
                        (3, portfolio()),
                        (4, blog()),
                        (5, contact()),
                    ),
                    width="95vw",
                    background_color="#222",
                    border_radius="30px",
                ),
                direction="column",
                spacing="2",
                align="center",
                justify="center",
            ),
            #barra_mobile(),
            drawer_mobile(),
            margin="30px",
        ),
        align="center",
        justify="center",
        min_height="100vh",
        
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    ),
    style={"breakpoints": ["30em", "48em", "1250px", "80em", "96em"]}
    )
app.add_page(index)
