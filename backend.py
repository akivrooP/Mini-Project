from flask import Flask, jsonify, request, render_template
from dc import  Db_operations

ipl = Db_operations()

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('h.html')

@app.route('/view')
def view_page():
    return render_template('View.html')

@app.route('/edit')
def edit_page():
    return render_template('Edit.html')


@app.route('/ipl')
def show_tables():
    tables=ipl.show_all_tables()
    table_dict=[]
    for table in tables:
        table_dict.append({'table':table})
    return jsonify(table_dict)
#---------------------------------------------------------------------1
@app.route('/ipl/addteam',methods=['POST'])
def add_team_row():
    body = request.get_json()
    tup=(body['team_id'],body['team_name'],body['city'],body['coach'],body['captain'],body['no_of_players'],body['no_of_staff'])
    row=ipl.add_team(tup)
    return jsonify(row)
  
@app.route('/ipl/delteam',methods=["DELETE"])  
def del_team_row():
    body = request.get_json()
    id=body['team_id']
    row=ipl.del_team(id)
    return jsonify(row)

@app.route('/ipl/upteam', methods=["POST"])
def update_team_row():
    body = request.get_json()
    tup = (body.get("team_name"),body.get("city"),body.get("coach"),body.get("captain"),body.get("no_of_players"),
        body.get("no_of_staff"),body.get("team_id"))
    print(body)
    row = ipl.update_team(tup)
    return jsonify(row)
#---------------------------------------------------------------------2
@app.route('/ipl/addplayer',methods=['POST'])
def add_player_row():
    body = request.get_json()
    tup=tuple(body.values())
    row=ipl.add_player(tup)
    return jsonify(row)

@app.route('/ipl/delplayer',methods=["DELETE"])  
def del_player_row():
    body = request.get_json()
    id=body['player_id']
    row=ipl.del_player(id)
    return jsonify(row)

@app.route('/ipl/upplayer', methods=["POST"])
def update_player_row():
    body = request.get_json()
    tup = (
        body.get("player_name"),
        body.get("team_id"),
        body.get("nationality"),
        body.get("role"),
        body.get("age"),
        body.get("player_id")
    )
    row = ipl.update_player(tup)
    return jsonify(row)

#---------------------------------------------------------------------3
@app.route('/ipl/addstadium',methods=['POST'])
def add_stadium_row():
    body = request.get_json()
    tup=tuple(body.values())
    row=ipl.add_stadium(tup)
    return jsonify(row)

@app.route('/ipl/delstadium',methods=["DELETE"])  
def del_stadium_row():
    body = request.get_json()
    id=body['stadium_id']
    row=ipl.del_stadium(id)
    return jsonify(row)

@app.route('/ipl/upstadium', methods=["POST"])
def update_stadium_row():
    body = request.get_json()
    tup = (
        body.get("stadium_name"),
        body.get("city"),
        body.get("capacity"),
        body.get("no_of_stands"),
        body.get("home_team_id"),
        body.get("stadium_id")
    )
    row = ipl.update_stadium(tup)
    return jsonify(row)

#---------------------------------------------------------------------4  
@app.route('/ipl/addplayer_stats',methods=['POST'])
def add_playerstats_row():
    body = request.get_json()
    tup=tuple(body.values())
    row=ipl.add_playerstats(tup)
    return jsonify(row)

@app.route('/ipl/delplayer_stats',methods=["DELETE"])  
def del_playerstats_row():
    body = request.get_json()
    id=body['player_id']
    row=ipl.del_playerstats(id)
    ipl.add_playerstats((id,'Batsman',0,0,0,0,0,0))
    return jsonify(row)     

#---------------------------------------------------------------------5
@app.route('/ipl/addmatch_stats',methods=['POST'])
def add_match_stats_row():
    body = request.get_json()
    tup=tuple(body.values())
    row=ipl.add_match_stats(tup)
    pid=ipl.get_player_id(tup[0])
    row=ipl.update_playerstats(tup,pid)
    return jsonify(row)

@app.route('/ipl/delmatch_stats',methods=["DELETE"])  
def del_match_stats_row():
    body = request.get_json()
    id=body['mid']
    name=body['pname']
    row=ipl.del_match_stats(name,id)
    return jsonify(row) 
#---------------------------------------------------------------------6
@app.route('/ipl/addmatches',methods=['POST'])
def add_match_row():
    body = request.get_json()
    tup=tuple(body.values())
    row=ipl.add_match(tup)
    return jsonify(row)

@app.route('/ipl/delmatches',methods=["DELETE"])  
def del_match_row():
    body = request.get_json()
    id=body['match_id']
    row=ipl.del_match(id)
    return jsonify(row)

@app.route('/ipl/upmatches', methods=["POST"])
def update_match_row():
    body = request.get_json()
    tup = (
        body.get("match_date"),
        body.get("team1_id"),
        body.get("team2_id"),
        body.get("venue"),
        body.get("winner_team_id"),
        body.get("match_id")
    )
    row = ipl.update_match(tup)
    return jsonify(row)
#-----------------------------------------------------display
@app.route('/ipl/display_table', methods=['POST'])
def display_table_rows():
    body = request.get_json()
    table = body.get('table_name')
    if table == 'player_stats':
        table='player_stats'
    if table == 'winners':
        data=ipl.get_all_winner_teams()
        columns = ['team_1', 'team_2', 'winner_team']
        result = [dict(zip(columns, row)) for row in data]

        return jsonify(result)
    print(table)
    display_list = ipl.display_table(table)
    columns = ipl.get_table_columns(table)
    

    if not display_list or not columns:
        return jsonify([])

    table_data = [dict(zip(columns, row)) for row in display_list]
    return jsonify(table_data)

@app.route('/ipl/winner_teams', methods=['GET'])
def get_winner_teams():
    teams = ipl.get_all_winner_teams()
    return jsonify(teams)


app.run(debug=True)