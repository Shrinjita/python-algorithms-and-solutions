import pandas as pd
from pathlib import Path
import bcrypt

# Define database path
path = Path("database")

def count_reset():
    voter_df = pd.read_csv(path / 'voterList.csv')
    voter_df['hasVoted'] = 0
    voter_df.to_csv(path / 'voterList.csv', index=False)

    cand_df = pd.read_csv(path / 'cand_list.csv')
    cand_df['Vote Count'] = 0
    cand_df.to_csv(path / 'cand_list.csv', index=False)

def reset_voter_list():
    df = pd.DataFrame(columns=['voter_id', 'Name', 'Gender', 'Aadhar Number', 'City', 'Passw', 'hasVoted'])
    df.to_csv(path / 'voterList.csv', index=False)

def reset_cand_list():
    df = pd.DataFrame(columns=['Sign', 'Name', 'Vote Count'])
    df.to_csv(path / 'cand_list.csv', index=False)

def verify(vid, passw):
    df = pd.read_csv(path / 'voterList.csv')
    user = df[df['voter_id'] == vid]
    if not user.empty:
        stored_hash = user.iloc[0]['Passw']
        return bcrypt.checkpw(passw.encode(), stored_hash.encode())
    return False

def isEligible(vid):
    df = pd.read_csv(path / 'voterList.csv')
    user = df[df['voter_id'] == vid]
    return not user.empty and user.iloc[0]['hasVoted'] == 0

def vote_update(st, vid):
    if isEligible(vid):
        df = pd.read_csv(path / 'cand_list.csv')
        df.loc[df['Sign'] == st, 'Vote Count'] += 1
        df.to_csv(path / 'cand_list.csv', index=False)
        
        voter_df = pd.read_csv(path / 'voterList.csv')
        voter_df.loc[voter_df['voter_id'] == vid, 'hasVoted'] = 1
        voter_df.to_csv(path / 'voterList.csv', index=False)
        
        return True
    return False

def show_result():
    df = pd.read_csv(path / 'cand_list.csv')
    return df.set_index('Sign')['Vote Count'].to_dict()

def isValidAadhar(aadhar):
    df = pd.read_csv(path / 'voterList.csv')
    return int(aadhar) not in df['voter_id'].values

def taking_data_voter(name, gender, aadhar, city, passw):
    if len(aadhar) == 12 and aadhar.isnumeric() and isValidAadhar(aadhar):
        hashed_pw = bcrypt.hashpw(passw.encode(), bcrypt.gensalt()).decode()
        new_voter = pd.DataFrame({
            "voter_id": [int(aadhar)],
            "Name": [name],
            "Gender": [gender],
            "Aadhar Number": [aadhar],
            "City": [city],
            "Passw": [hashed_pw],
            "hasVoted": [0]
        })
        df = pd.read_csv(path / 'voterList.csv')
        df = pd.concat([df, new_voter], ignore_index=True)
        df.to_csv(path / 'voterList.csv', index=False)
        return aadhar
    return -1