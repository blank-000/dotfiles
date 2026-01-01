import QtQuick

Item {
    required property real s
    required property real m_offset
    required property color accentColor
    required property int bars
    implicitWidth: 100 * s
    implicitHeight: 100 * s

    x: s
    y: (m_offset + 1308) * s

    Column {
        anchors.fill: parent
        spacing: 6 * s 

        Repeater {
            model: 5
            Rectangle {
                anchors.horizontalCenter: parent.horizontalCenter
                implicitHeight: 12 * s
                radius: 3 * s

                implicitWidth: index < 5-bars
                    ? 40 * s : 80 * s
                color: index < 5-bars
                    ? Qt.rgba( accentColor.r, accentColor.g, accentColor.b , .05 )
                    : Qt.rgba( accentColor.r, accentColor.g, accentColor.b , .5 )
            }
        }
    }
}
