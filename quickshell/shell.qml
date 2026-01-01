import Quickshell
import Quickshell.Hyprland
import QtQuick
import Quickshell.Services.UPower

Variants {
    model: Quickshell.screens

    delegate: Component {
        PanelWindow {
            id: root

            required property var modelData
            screen: modelData

            /* ---------- scaling ---------- */
            property real monitor_scale: modelData.name === "eDP-1" ? 1.6 : 1.0
            property real s: 1.0/monitor_scale
            property int monitor_offset: modelData.name === "eDP-1" ? 200 : 0

            /* ---------- battery upower ------------ */
            property bool isDischarging: UPower.onBattery
            property int step: 20
            property int percent: Math.round(UPower.displayDevice.percentage * 100)
            property int bars: Math.floor(percent / step) + 1

            /* ---------- workspace colors ---------- */
            readonly property var workspaceColors: [
                "#A7C080",
                "#83C092",
                "#DBBC7F",
                "#E69875",
                "#E67E80"
            ]
            property int currentWorkspace: 1
            readonly property color accentColor: workspaceColors[currentWorkspace - 1]

            /* ---------- positioning ---------- */
            color: "transparent"

            anchors.top: true
            anchors.right: true
            anchors.bottom: true
            anchors.left: true

            exclusiveZone: 0
            aboveWindows: false
            focusable: false


            /* ---------- battery tracking ---------- */
            Connections {
                target: UPower

                function onOnBatteryChanged() {
                    root.isDischarging = UPower.onBattery
                }
            }

            Connections {
                target: UPower.displayDevice

                function onPercentageChanged() {
                    root.percent = Math.round(UPower.displayDevice.percentage * 100)
                    root.bars = Math.floor(root.percent / root.step) + 1
                    console.log("current charge:", root.percent, "\n bars to show: ", root.bars)
                }
            }

            /* ---------- workspace tracking ---------- */
            Connections {
                target: Hyprland
                function onRawEvent(ev) {
                    if (ev.name !== "workspacev2")
                    return

                    const args = ev.parse(2)
                    const rawId = parseInt(args[0])
                    if (rawId <= 0)
                    return

                    const normalized = ((rawId - 1) % 10) + 1
                    root.currentWorkspace = ((normalized - 1) % 5) + 1
                }
            }

            /* ---------- widgets (ITEMS) ---------- */

            ClockItem {
                s: root.s
                accentColor: root.accentColor
                m_offset: monitor_offset
            }

            BatteryItem {
                id: battery_display
                visible: root.isDischarging
                s: root.s
                bars: root.bars
                accentColor: root.accentColor
                m_offset: monitor_offset
            }

        }
    }
}

