'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Location extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      Location.belongsTo(models.User,{
        foreignKey:"userId",
        
      })
    }
  }
  
  Location.init({
    name: DataTypes.STRING,
    link: DataTypes.STRING,
    latitude: DataTypes.FLOAT,
    longitude: DataTypes.FLOAT,
    state: DataTypes.STRING,
    type: DataTypes.STRING,
    region: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Location',
  });
  return Location;
};