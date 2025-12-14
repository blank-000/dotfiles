import Quickshell
import Quickshell.Hyprland
import QtQuick

Variants {
    model: Quickshell.screens;
    delegate: Component {
        PanelWindow {
            id:root

            required property var modelData
            screen: modelData

            property real monitor_scale: modelData.name === "eDP-1" ? 1.6 : 1.0
            property real s: 1.0/monitor_scale
            property int monitor_offset: modelData.name === "eDP-1" ? 200 : 0

            readonly property var workspaceColors: [
                "#A7C080",
                "#83C092",
                "#DBBC7F",
                "#E69875",
                "#E67E80"
            ]

            property int currentWorkspace: 1
            property color text_color: workspaceColors[currentWorkspace - 1]

            implicitWidth: 200 * s
            implicitHeight: 100 * s

            color: "transparent"

            anchors.top: true
            anchors.right: true
            margins.top:  (1206 + monitor_offset) * s
            margins.right: 60 * s

            exclusiveZone: 0
            aboveWindows: false
            focusable: false

            Text {
                anchors.centerIn: parent
                text: Time.time
                color: root.text_color
                font.family: "Loaded"
                font.pixelSize: 62 * s
            }
            Connections {
                target: Hyprland

                // AI WUZ HEAR
                function onRawEvent(ev) {
                    if (ev.name !== "workspacev2")
                        return

                    // WORKSPACEID,WORKSPACENAME
                    const args = ev.parse(2)
                    const rawId = parseInt(args[0])
                    if (rawId <= 0)
                        return

                    // bind 1–10 → 1–5
                    const normalized = ((rawId - 1) % 10) + 1
                    const ws = ((normalized - 1) % 5) + 1

                    root.currentWorkspace = ws
                }
            }
        }
    }
}

