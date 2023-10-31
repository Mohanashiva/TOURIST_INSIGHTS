'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.addColumn('Locations', 'state', {
      type: Sequelize.STRING,
      allowNull: true, // Modify this based on your requirements
    });
    await queryInterface.addColumn('Locations', 'type', {
      type: Sequelize.STRING,
      allowNull: true, // Modify this based on your requirements
    });
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
