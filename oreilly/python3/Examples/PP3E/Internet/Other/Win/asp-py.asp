<HTML><BODY>
<%@ Language=Python %>
     
<%
#
# Python code here, using global names Request (input), Response (output), etc.
#
Response.Write("Hello ASP World from URL %s" % 
                          Request.ServerVariables("PATH_INFO"))
%>
</BODY></HTML>
