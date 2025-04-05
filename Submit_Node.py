from BaseNode import BaseNode




class Submit_Node(BaseNode):
    def __init__(self, ip, port, name):
        BaseNode.__init__(self, ip=ip, port=port, name=name, type="SUBMIT")


        @self.app.route("/gui/submit")
        def gui_submit():
            