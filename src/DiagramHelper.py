from StringBuilder import StringBuilder
import untangle

from src.Labels import L


def make_list_from_attr(o, s):
    if hasattr(o, s) and not isinstance(getattr(o, s), list):
        setattr(o, s, list(getattr(o, s)))


def prepareDiagram(diagram):
    make_list_from_attr(diagram, 'widget')

    for w in diagram.widget:
        for s in ['action', 'event', 'incoming', 'outgoing']:
            make_list_from_attr(w, s)
    return diagram


class DiagramHelper:

    def parseDiagram(self, xml_file: str):
        d = untangle.parse(xml_file).diagram
        d = prepareDiagram(d)
        return d

    def convertDiagramToDot(self, diagram, file_str: str) -> None:
        with open(file_str, 'w') as writer:
            graphName = diagram.name
            print("digraph " + graphName.cdata + " {", file=writer)
            print("\trankdir = LR;", file=writer)

            for widget in diagram.widget:
                if widget['type'] == L.L_WIDGET_STATE:
                    print("\t" + L.PREFIX + widget['id'] + " [label=\"" + widget.attributes.name.cdata + "\"]",
                          file=writer)
                    if hasattr(widget.attributes, 'incoming') and widget.attributes.incoming is not None:
                        for incoming in widget.attributes.incoming:
                            print("\t" + L.PREFIX + incoming['id'] + " -> " + L.PREFIX + widget['id'] + ";",
                                  file=writer)

                    if hasattr(widget.attributes, 'outgoing') and widget.attributes.outgoing is not None:
                        for outgoing in widget.attributes.outgoing:
                            print("\t" + L.PREFIX + widget['id'] + " -> " + L.PREFIX + outgoing['id'] + ";",
                                  file=writer)
                elif widget['type'] == L.L_WIDGET_TRANSITION:
                    print("\t" + L.PREFIX + widget['id'] + " [shape=\"none\", label=<" + self.getLabelByTransition(
                        widget) + ">]",
                          file=writer)

            print("}", file=writer)

    def getLabelByTransition(self, transition) -> str:
        attr = transition.attributes
        sb = StringBuilder()
        sb.append("<table>")
        sb.append("<tr><td>Event</td><td>")
        sb.append(attr.event['name'])
        sb.append("</td></tr>")
        sb.append("<tr><td colspan=\"2\">")
        sb.append(attr.event['comment'])
        sb.append("</td></tr>")
        if hasattr(attr, 'action'):
            sb.append("<tr><td colspan=\"2\">Actions:</td></tr>")
            actions = attr.action
            # ETO GENIAL'NO
            if not isinstance(actions, list):
                actions = [actions]
            for i in range(len(actions)):
                action = actions[i]
                sb.append("<tr><td>")
                sb.append(str(i + 1))
                sb.append(".</td><td>")
                sb.append(action['name'])
                sb.append("</td></tr>")

        if hasattr(attr, 'guard') and hasattr(attr.guard, 'cdata') and attr.guard.cdata:
            guard = attr.guard.cdata.replace("&", "&amp;")
            sb.append("<tr><td>Guard</td><td><font color=\"red\">")
            sb.append(guard)
            sb.append("</font></td></tr>")

        sb.append("</table>")
        return sb.to_string()
