'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Data extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  Data.init({
    name: DataTypes.STRING,
    description: DataTypes.STRING,
    region: DataTypes.STRING,
    type: DataTypes.STRING,
    mapsLink: DataTypes.STRING,
    longitude: DataTypes.FLOAT,
    latitude: DataTypes.FLOAT,
    price: DataTypes.INTEGER,
    duration: DataTypes.INTEGER,
    state: DataTypes.STRING,
    
  }, {
    sequelize,
    modelName: 'Data',
  });
  return Data;
};