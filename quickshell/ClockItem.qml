import QtQuick

Item {
    required property real s
    required property color accentColor
    required property real m_offset

    width: 200 * s
    height: 100 * s
    x: 2304 * s
    y: (m_offset + 1206) * s

    Text {
        anchors.centerIn: parent
        text: Time.time
        color: accentColor
        font.family: "Loaded"
        font.pixelSize: 62 * s
    }
}
