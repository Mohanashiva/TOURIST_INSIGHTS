'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class User extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // Define the association with Location model
      User.hasMany(models.Location, {
        foreignKey: "userId",
      });

      // Define the association with Resource model
      User.hasMany(models.Resource, {
        foreignKey: "userId",
      });
    }
  }

  User.init(
    {
      firstName: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          notNull: true,
        },
      },
      lastName: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          notNull: true,
        },
      },
      email: {
        type: DataTypes.STRING,
        unique:true,
        allowNull: false,
        validate: {
          notNull: true,
        },
      },
      password: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          notNull: true,
        },
      },
    },
    {
      sequelize,
      modelName: "User",
    }
  );
  return User;
};