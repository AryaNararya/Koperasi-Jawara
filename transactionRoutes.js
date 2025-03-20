const express = require('express');
const Transaction = require('../models/Transaction');

const router = express.Router();

// Halaman utama - daftar transaksi
router.get('/', async (req, res) => {
    const transactions = await Transaction.find().sort({ date: -1 });
    res.render('index', { transactions });
});

// Halaman tambah transaksi
router.get('/add', (req, res) => {
    res.render('addTransaction');
});

// Proses tambah transaksi
router.post('/add', async (req, res) => {
    const { description, amount, type } = req.body;
    await Transaction.create({ description, amount, type });
    res.redirect('/');
});

// Halaman edit transaksi
router.get('/edit/:id', async (req, res) => {
    const transaction = await Transaction.findById(req.params.id);
    res.render('editTransaction', { transaction });
});

// Proses edit transaksi
router.put('/edit/:id', async (req, res) => {
    const { description, amount, type } = req.body;
    await Transaction.findByIdAndUpdate(req.params.id, { description, amount, type });
    res.redirect('/');
});

// Hapus transaksi
router.delete('/delete/:id', async (req, res) => {
    await Transaction.findByIdAndDelete(req.params.id);
    res.redirect('/');
});

module.exports = router;
