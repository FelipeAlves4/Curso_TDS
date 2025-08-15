import 'package:flutter/material.dart';
import 'package:intl/intl.dart'; // Pacote para formatação de datas. Adicione `intl: ^0.19.0` ao seu pubspec.yaml
import 'dart:math'; // Para calcular o IMC

// 1. PONTO DE ENTRADA DO APLICATIVO
void main() {
  runApp(const MeuAppSaude());
}

// 2. WIDGET RAIZ DO APLICATIVO
class MeuAppSaude extends StatelessWidget {
  const MeuAppSaude({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'App de Saúde Responsivo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.teal,
        visualDensity: VisualDensity.adaptivePlatformDensity,
        scaffoldBackgroundColor: const Color(0xFFF5F7FA),
         inputDecorationTheme: InputDecorationTheme(
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12.0),
            borderSide: const BorderSide(color: Colors.grey),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12.0),
            borderSide: const BorderSide(color: Colors.teal, width: 2.0),
          ),
        ),
      ),
      home: const TelaPrincipalResponsiva(),
    );
  }
}

// 3. TELA PRINCIPAL - GERENCIA A NAVEGAÇÃO ENTRE ABAS
class TelaPrincipalResponsiva extends StatefulWidget {
  const TelaPrincipalResponsiva({super.key});

  @override
  State<TelaPrincipalResponsiva> createState() => _TelaPrincipalResponsivaState();
}

class _TelaPrincipalResponsivaState extends State<TelaPrincipalResponsiva> {
  int _selectedIndex = 0;

  // MODIFICAÇÃO: Substituímos o placeholder pela nova tela de Perfil
  static const List<Widget> _widgetOptions = <Widget>[
    DashboardContent(),
    HistoricoScreen(),
    ProfileScreen(), // <<< TELA DE PERFIL INTEGRADA AQUI
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    final double screenWidth = MediaQuery.of(context).size.width;
    const double breakpoint = 600.0;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Painel de Saúde'),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications_none),
            onPressed: () {},
          ),
        ],
      ),
      body: _widgetOptions.elementAt(_selectedIndex),
      bottomNavigationBar: screenWidth < breakpoint
          ? BottomNavigationBar(
              items: const <BottomNavigationBarItem>[
                BottomNavigationBarItem(icon: Icon(Icons.home_outlined), activeIcon: Icon(Icons.home), label: 'Início'),
                BottomNavigationBarItem(icon: Icon(Icons.history_outlined), activeIcon: Icon(Icons.history), label: 'Histórico'),
                BottomNavigationBarItem(icon: Icon(Icons.person_outline), activeIcon: Icon(Icons.person), label: 'Perfil'),
              ],
              currentIndex: _selectedIndex,
              selectedItemColor: Colors.teal,
              onTap: _onItemTapped,
            )
          : null,
    );
  }
}

// 4. CONTEÚDO DO PAINEL PRINCIPAL
class DashboardContent extends StatelessWidget {
  const DashboardContent({super.key});
 
  // (O código desta seção permanece o mesmo da resposta anterior)
  @override
  Widget build(BuildContext context) {
    final double screenWidth = MediaQuery.of(context).size.width;
    const double breakpoint = 600.0;
    final int crossAxisCount = screenWidth < breakpoint ? 2 : 4;

    return CustomScrollView(
      slivers: [
        SliverToBoxAdapter(
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Olá, Usuário!', style: Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.bold)),
                const SizedBox(height: 4),
                const Text('Aqui está um resumo da sua atividade hoje.', style: TextStyle(color: Colors.black54)),
              ],
            ),
          ),
        ),
        SliverPadding(
          padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
          sliver: SliverGrid(
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: crossAxisCount,
              mainAxisSpacing: 16.0,
              crossAxisSpacing: 16.0,
              childAspectRatio: 1.0,
            ),
            delegate: SliverChildBuilderDelegate(
              (context, index) {
                final item = healthData[index];
                return HealthCard(
                  title: item['title'] as String,
                  value: item['value'] as String,
                  icon: item['icon'] as IconData,
                  color: item['color'] as Color,
                );
              },
              childCount: healthData.length,
            ),
          ),
        ),
        SliverToBoxAdapter(
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                textStyle: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const NovaAtividadeScreen()),
                );
              },
              icon: const Icon(Icons.add),
              label: const Text("Registrar Nova Atividade"),
            ),
          ),
        ),
      ],
    );
  }
}

// =======================================================================
//                       NOVA TELA: PERFIL
// =======================================================================
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Dados fictícios do perfil
    const String userName = "Alex Green";
    const String userEmail = "alex.green@example.com";
    const double userHeight = 1.75; // em metros
    const double userWeight = 72; // em kg

    // Cálculo do IMC (Índice de Massa Corporal)
    final double imc = userWeight / (pow(userHeight, 2));

    return ListView(
      padding: const EdgeInsets.symmetric(vertical: 20.0),
      children: [
        _buildProfileHeader(userName, userEmail),
        const SizedBox(height: 30),
        _buildStatsCard(userHeight, userWeight, imc),
        const SizedBox(height: 20),
        _buildOptionsCard(context),
        const SizedBox(height: 20),
        _buildLogoutButton(context),
      ],
    );
  }

  // Widget para o cabeçalho do perfil
  Widget _buildProfileHeader(String name, String email) {
    return Column(
      children: [
        const CircleAvatar(
          radius: 50,
          backgroundColor: Colors.teal,
          child: Icon(Icons.person, size: 60, color: Colors.white),
        ),
        const SizedBox(height: 12),
        Text(
          name,
          style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 4),
        Text(
          email,
          style: const TextStyle(fontSize: 16, color: Colors.grey),
        ),
      ],
    );
  }

  // Widget para o card de estatísticas (Peso, Altura, IMC)
  Widget _buildStatsCard(double height, double weight, double imc) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20.0),
      child: Card(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 20.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildStatItem("Altura", "${(height * 100).toInt()} cm"),
              _buildStatItem("Peso", "${weight.toInt()} kg"),
              _buildStatItem("IMC", imc.toStringAsFixed(1)), // Formata para 1 casa decimal
            ],
          ),
        ),
      ),
    );
  }
 
  // Item individual de estatística
  Widget _buildStatItem(String label, String value) {
    return Column(
      children: [
        Text(value, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
        const SizedBox(height: 4),
        Text(label, style: const TextStyle(color: Colors.grey)),
      ],
    );
  }

  // Widget para o card de opções
  Widget _buildOptionsCard(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20.0),
      child: Card(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        child: Column(
          children: [
            _buildOptionTile(context, icon: Icons.settings_outlined, title: "Configurações da Conta", onTap: () {}),
            const Divider(height: 1, indent: 16, endIndent: 16),
            _buildOptionTile(context, icon: Icons.notifications_outlined, title: "Notificações", onTap: () {}),
            const Divider(height: 1, indent: 16, endIndent: 16),
            _buildOptionTile(context, icon: Icons.lock_outline, title: "Privacidade", onTap: () {}),
            const Divider(height: 1, indent: 16, endIndent: 16),
            _buildOptionTile(context, icon: Icons.help_outline, title: "Ajuda e Suporte", onTap: () {}),
          ],
        ),
      ),
    );
  }

  // ListTile reutilizável para as opções
  Widget _buildOptionTile(BuildContext context, {required IconData icon, required String title, required VoidCallback onTap}) {
    return ListTile(
      leading: Icon(icon, color: Colors.teal),
      title: Text(title),
      trailing: const Icon(Icons.arrow_forward_ios, size: 16, color: Colors.grey),
      onTap: onTap,
    );
  }

  // Widget para o botão de sair
  Widget _buildLogoutButton(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20.0),
      child: ElevatedButton.icon(
        icon: const Icon(Icons.logout),
        label: const Text("Sair da Conta"),
        onPressed: () {
          // Lógica para logout
        },
        style: ElevatedButton.styleFrom(
          foregroundColor: Colors.red, backgroundColor: Colors.red.shade50,
          padding: const EdgeInsets.symmetric(vertical: 16),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ),
    );
  }
}

// =======================================================================
//               TELAS E WIDGETS DAS SEÇÕES ANTERIORES
// (As telas de Histórico, Nova Atividade e os dados fictícios permanecem
// exatamente como na resposta anterior, sem nenhuma alteração)
// =======================================================================

// TELA DE HISTÓRICO
class HistoricoScreen extends StatelessWidget {
  const HistoricoScreen({super.key});

  IconData _getIconForActivity(String activity) {
    switch (activity) {
      case 'Corrida': return Icons.directions_run;
      case 'Musculação': return Icons.fitness_center;
      case 'Natação': return Icons.pool;
      case 'Caminhada': return Icons.directions_walk;
      default: return Icons.help_outline;
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      padding: const EdgeInsets.all(16.0),
      itemCount: historicoAtividades.length,
      itemBuilder: (context, index) {
        final activity = historicoAtividades[index];
        return Card(
          elevation: 2,
          margin: const EdgeInsets.only(bottom: 12.0),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          child: ListTile(
            contentPadding: const EdgeInsets.symmetric(vertical: 10, horizontal: 16),
            leading: CircleAvatar(
              backgroundColor: Colors.teal.shade100,
              child: Icon(_getIconForActivity(activity['tipo']), color: Colors.teal),
            ),
            title: Text(activity['tipo'], style: const TextStyle(fontWeight: FontWeight.bold)),
            subtitle: Text("${activity['data']} - ${activity['duracao']} min", style: const TextStyle(color: Colors.black54)),
            trailing: Text("${activity['calorias']} kcal", style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.orange, fontSize: 16)),
          ),
        );
      },
    );
  }
}

// TELA DE NOVA ATIVIDADE
class NovaAtividadeScreen extends StatefulWidget {
  const NovaAtividadeScreen({super.key});
  @override
  State<NovaAtividadeScreen> createState() => _NovaAtividadeScreenState();
}

class _NovaAtividadeScreenState extends State<NovaAtividadeScreen> {
  final _formKey = GlobalKey<FormState>();
  String? _selectedActivity;
  DateTime? _selectedDate;
  final TextEditingController _durationController = TextEditingController();
  final TextEditingController _caloriesController = TextEditingController();

  @override
  void dispose() {
    _durationController.dispose();
    _caloriesController.dispose();
    super.dispose();
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(context: context, initialDate: _selectedDate ?? DateTime.now(), firstDate: DateTime(2020), lastDate: DateTime.now());
    if (picked != null && picked != _selectedDate) {
      setState(() => _selectedDate = picked);
    }
  }

  void _submitForm() {
    if ((_formKey.currentState?.validate() ?? false) && _selectedDate != null) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Atividade salva com sucesso!'), backgroundColor: Colors.green));
      Navigator.pop(context);
    } else if (_selectedDate == null) {
       ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Por favor, selecione uma data.'), backgroundColor: Colors.red.shade400));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Registrar Nova Atividade')),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: const EdgeInsets.all(20.0),
          children: <Widget>[
            DropdownButtonFormField<String>(
              value: _selectedActivity,
              decoration: const InputDecoration(labelText: 'Tipo de Atividade'),
              items: ['Caminhada', 'Corrida', 'Musculação', 'Natação'].map((label) => DropdownMenuItem(child: Text(label), value: label)).toList(),
              onChanged: (value) => setState(() => _selectedActivity = value),
              validator: (value) => value == null ? 'Por favor, selecione uma atividade.' : null,
            ),
            const SizedBox(height: 20),
            TextFormField(
              controller: _durationController,
              decoration: const InputDecoration(labelText: 'Duração (em minutos)'),
              keyboardType: TextInputType.number,
              validator: (value) {
                if (value == null || value.isEmpty) return 'Por favor, insira a duração.';
                if (int.tryParse(value) == null) return 'Por favor, insira um número válido.';
                return null;
              },
            ),
            const SizedBox(height: 20),
            TextFormField(
              controller: _caloriesController,
              decoration: const InputDecoration(labelText: 'Calorias Queimadas (kcal)'),
              keyboardType: TextInputType.number,
              validator: (value) {
                if (value == null || value.isEmpty) return 'Por favor, insira as calorias.';
                if (int.tryParse(value) == null) return 'Por favor, insira um número válido.';
                return null;
              },
            ),
            const SizedBox(height: 20),
            ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 12),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12), side: BorderSide(color: Colors.grey.shade400)),
              title: Text(_selectedDate == null ? 'Selecione a Data' : DateFormat('dd/MM/yyyy', 'pt_BR').format(_selectedDate!)),
              trailing: const Icon(Icons.calendar_today),
              onTap: () => _selectDate(context),
            ),
            const SizedBox(height: 30),
            ElevatedButton(
              onPressed: _submitForm,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16), textStyle: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              child: const Text('Salvar'),
            ),
          ],
        ),
      ),
    );
  }
}

// WIDGETS E DADOS AUXILIARES
class HealthCard extends StatelessWidget {
  final String title, value; final IconData icon; final Color color;
  const HealthCard({super.key, required this.title, required this.value, required this.icon, required this.color});
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(color: color.withOpacity(0.15), borderRadius: BorderRadius.circular(16), border: Border.all(color: color.withOpacity(0.3))),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Icon(icon, size: 32, color: color),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: TextStyle(fontWeight: FontWeight.bold, color: color, fontSize: 16)),
                Text(value, style: const TextStyle(fontWeight: FontWeight.w900, color: Colors.black87, fontSize: 20)),
              ],
            )
          ],
        ),
      ),
    );
  }
}

final List<Map<String, dynamic>> healthData = [
  {'title': 'Batimentos', 'value': '78 bpm', 'icon': Icons.favorite_border, 'color': Colors.red},
  {'title': 'Passos', 'value': '4.582', 'icon': Icons.directions_walk, 'color': Colors.blue},
  {'title': 'Calorias', 'value': '1.200 kcal', 'icon': Icons.local_fire_department_outlined, 'color': Colors.orange},
  {'title': 'Sono', 'value': '7h 32m', 'icon': Icons.bedtime_outlined, 'color': Colors.purple},
  {'title': 'Água', 'value': '1.5 L', 'icon': Icons.water_drop_outlined, 'color': Colors.cyan},
  {'title': 'Meditação', 'value': '15 min', 'icon': Icons.self_improvement_outlined, 'color': Colors.green},
];

final List<Map<String, dynamic>> historicoAtividades = [
  {'tipo': 'Corrida', 'data': '14/08/2025', 'duracao': 30, 'calorias': 250},
  {'tipo': 'Musculação', 'data': '13/08/2025', 'duracao': 60, 'calorias': 300},
  {'tipo': 'Caminhada', 'data': '13/08/2025', 'duracao': 45, 'calorias': 150},
  {'tipo': 'Natação', 'data': '11/08/2025', 'duracao': 50, 'calorias': 400},
  {'tipo': 'Corrida', 'data': '10/08/2025', 'duracao': 25, 'calorias': 200},
];
