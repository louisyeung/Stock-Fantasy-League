from flask_restful import reqparse, abort, Resource
import json
class League(Resource):
    @staticmethod  # getLeagueInfo
    #Getting league info from specified league
    def get(cur, LID):

        cur.execute("SELECT * FROM leagues WHERE lid = %s;", [LID])
        return json.dumps({"Leagues": cur.fetchall()})
        pass
