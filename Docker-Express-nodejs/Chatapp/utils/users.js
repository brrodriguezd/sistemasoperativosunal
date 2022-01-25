const users = [];

// Join user to chat
function userJoin(id, username, room, anonimo) {
  if (anonimo == 'Si'){
    username = 'anonimo';
  }
  const user = { id, username, room};

  users.push(user);

  return user;
}

// Get current user
function getCurrentUser(id) {
  return users.find(user => user.id === id);
}

// User leaves chat
function userLeave(id) {
  const index = users.findIndex(user => user.id === id);

  if (index !== -1) {
    return users.splice(index, 1)[0];
  }
}

// Get room users
function getRoomUsers(user) {
  return users.filter(users => users.room === user.room);
}

module.exports = {
  userJoin,
  getCurrentUser,
  userLeave,
  getRoomUsers
};
