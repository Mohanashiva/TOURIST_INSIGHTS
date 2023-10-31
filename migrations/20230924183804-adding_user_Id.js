'use strict';

const { sequelize } = require('../models');

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.addColumn("Locations","userId",{
      type:Sequelize.DataTypes.INTEGER
    })

    await queryInterface.addConstraint("Locations",{
      fields:["userId"],
      type:'foreign key',
      references:{
        table:"Users",
        field:"id"
      }
    })
    /**
     * 
     * 
     * Add altering commands here.
     *
     * Example:
     * await queryInterface.createTable('users', { id: Sequelize.INTEGER });
     */
  },

  async down (queryInterface, Sequelize) {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
  }
};
