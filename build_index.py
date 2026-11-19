import base64
with open(r'fonts/GoodDogPlain.ttf', 'rb') as f:
    b64_font = base64.b64encode(f.read()).decode('ascii')

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SWE Exam 3 Interactive Trainer | CSC 4350 / 6350</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <!-- Google Fonts Fallbacks -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;500&family=Kalam:wght@300;400&family=Patrick+Hand&display=swap" rel="stylesheet">
  
  <style>
                    /* User Custom Font: GoodDog Plain (both local file and embedded base64 fallback) */
    @font-face {
      font-family: 'GoodDog Plain';
      src: url('./fonts/GoodDogPlain.ttf') format('truetype'),
           url(data:font/truetype;charset=utf-8;base64,__B64_FONT__) format('truetype');
      font-weight: normal;
      font-style: normal;
      font-display: swap;
    }

    /* Pure Handwritten Font, Completely Unbolded, Natural Pen Look */
    .font-pure-notes {
      font-family: 'GoodDog Plain', 'GoodDogPlain', 'Kalam', 'Patrick Hand', 'Caveat', cursive, sans-serif;
      font-weight: 400;
      color: #0f172a;
    }

    /* Unstructured Organic Cram Sheet: Non-linear, Asymmetric Streams */
    .hw-stream-side1 {
      display: grid;
      grid-template-columns: 1.08fr 0.94fr 1.02fr;
      column-gap: 13px;
      font-size: 8.3pt;
      line-height: 1.14;
    }
    .hw-stream-side2 {
      display: grid;
      grid-template-columns: 0.96fr 1.06fr 1.02fr;
      column-gap: 12px;
      font-size: 8.3pt;
      line-height: 1.14;
    }

    /* Organic Handwritten Blobs (no bullets, no rigid outlines, natural flow) */
    .hw-blob {
      display: block;
      text-align: left;
    }

    /* Organic Angle & Offset Variations (Noticeable handwritten tilts & wandering margins) */
    .hw-b-1  { transform: rotate(-1.2deg); transform-origin: top left; margin-left: -5px; font-size: 8.5pt; line-height: 1.16; letter-spacing: -0.05px; margin-bottom: 12px; }
    .hw-b-2  { transform: rotate(1.4deg);  transform-origin: top left; margin-left: 9px;  font-size: 8.1pt; line-height: 1.12; letter-spacing: -0.15px; margin-bottom: 14px; }
    .hw-b-3  { transform: rotate(-0.8deg); transform-origin: top left; margin-left: -2px; font-size: 8.4pt; line-height: 1.15; letter-spacing: 0.05px;  margin-bottom: 11px; }
    .hw-b-4  { transform: rotate(1.1deg);  transform-origin: top left; margin-left: 6px;  font-size: 8.2pt; line-height: 1.13; letter-spacing: -0.10px; margin-bottom: 15px; }
    .hw-b-5  { transform: rotate(-1.4deg); transform-origin: top left; margin-left: -4px; font-size: 8.0pt; line-height: 1.11; letter-spacing: -0.18px; margin-bottom: 10px; }
    .hw-b-6  { transform: rotate(0.95deg); transform-origin: top left; margin-left: 7px;  font-size: 8.4pt; line-height: 1.14; letter-spacing: 0.08px;  margin-bottom: 13px; }
    .hw-b-7  { transform: rotate(-1.1deg); transform-origin: top left; margin-left: -3px; font-size: 8.1pt; line-height: 1.12; letter-spacing: -0.12px; margin-bottom: 11px; }
    .hw-b-8  { transform: rotate(1.5deg);  transform-origin: top left; margin-left: 8px;  font-size: 8.3pt; line-height: 1.15; letter-spacing: -0.05px; margin-bottom: 12px; }

    .hw-b-9  { transform: rotate(1.3deg);  transform-origin: top left; margin-left: 7px;  font-size: 8.4pt; line-height: 1.15; letter-spacing: -0.05px; margin-bottom: 12px; }
    .hw-b-10 { transform: rotate(-1.3deg); transform-origin: top left; margin-left: -5px; font-size: 8.1pt; line-height: 1.11; letter-spacing: -0.15px; margin-bottom: 13px; }
    .hw-b-11 { transform: rotate(0.9deg);  transform-origin: top left; margin-left: 6px;  font-size: 8.3pt; line-height: 1.14; letter-spacing: 0.05px;  margin-bottom: 11px; }
    .hw-b-12 { transform: rotate(-1.5deg); transform-origin: top left; margin-left: -3px; font-size: 8.0pt; line-height: 1.10; letter-spacing: -0.20px; margin-bottom: 14px; }
    .hw-b-13 { transform: rotate(1.2deg);  transform-origin: top left; margin-left: 9px;  font-size: 8.3pt; line-height: 1.13; letter-spacing: -0.08px; margin-bottom: 12px; }
    .hw-b-14 { transform: rotate(-1.0deg); transform-origin: top left; margin-left: -2px; font-size: 8.2pt; line-height: 1.12; letter-spacing: 0.04px;  margin-bottom: 11px; }
    .hw-b-15 { transform: rotate(1.4deg);  transform-origin: top left; margin-left: 5px;  font-size: 8.1pt; line-height: 1.11; letter-spacing: -0.14px; margin-bottom: 13px; }
    .hw-b-16 { transform: rotate(-1.2deg); transform-origin: top left; margin-left: -4px; font-size: 8.4pt; line-height: 1.14; letter-spacing: -0.06px; margin-bottom: 12px; }

    /* Print Specific Rules: Strict 2-Page Double Sided Sheet */
    @media print {
      body * { visibility: hidden; }
      #cheat-sheet-print-area, #cheat-sheet-print-area * { visibility: visible; }
      #cheat-sheet-print-area {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 0.12in;
        font-size: 8.2pt;
        line-height: 1.15;
        color: #0f172a !important;
      }
      .page-break { page-break-before: always; }
      .no-print { display: none !important; }
      @page {
        size: letter portrait;
        margin: 0.15in;
      }
    }

    /* Interactive diagram boxes for tabs */
    .uml-box { border: 2px solid #334155; border-radius: 4px; background: #ffffff; }
    .uml-header { background: #f1f5f9; border-bottom: 2px solid #334155; padding: 6px; font-weight: bold; text-align: center; }
    .uml-section { border-bottom: 1px solid #94a3b8; padding: 6px 10px; font-family: monospace; font-size: 12px; min-height: 44px; }
    .uml-section:last-child { border-bottom: none; }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 font-sans min-h-screen flex flex-col">

  <!-- Header -->
  <header class="bg-indigo-900 text-white shadow-lg sticky top-0 z-50 no-print">
    <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center space-x-3">
        <i data-lucide="graduation-cap" class="w-8 h-8 text-amber-400"></i>
        <div>
          <h1 class="text-xl font-bold tracking-tight">SWE Exam 3 Practice Suite</h1>
          <p class="text-xs text-indigo-200">GSU CSC 4350 / 6350 • Dr. Tushara Sadasivuni • Exam: Nov 19</p>
        </div>
      </div>
      <!-- Tab Navigation -->
      <nav class="flex space-x-1 bg-indigo-950/60 p-1 rounded-xl text-xs sm:text-sm font-medium">
        <button onclick="switchTab('quiz')" id="tab-btn-quiz" class="tab-btn px-3 py-1.5 rounded-lg transition-colors bg-indigo-600 text-white flex items-center gap-1.5">
          <i data-lucide="help-circle" class="w-4 h-4"></i> Section A: MCQs
        </button>
        <button onclick="switchTab('uml')" id="tab-btn-uml" class="tab-btn px-3 py-1.5 rounded-lg transition-colors text-indigo-200 hover:text-white flex items-center gap-1.5">
          <i data-lucide="layout-grid" class="w-4 h-4"></i> 8 In-Class UML Diagrams
        </button>
        <button onclick="switchTab('architecture')" id="tab-btn-architecture" class="tab-btn px-3 py-1.5 rounded-lg transition-colors text-indigo-200 hover:text-white flex items-center gap-1.5">
          <i data-lucide="network" class="w-4 h-4"></i> Architecture Models
        </button>
        <button onclick="switchTab('testcases')" id="tab-btn-testcases" class="tab-btn px-3 py-1.5 rounded-lg transition-colors text-indigo-200 hover:text-white flex items-center gap-1.5">
          <i data-lucide="check-square" class="w-4 h-4"></i> 5 Test Cases Builder
        </button>
        <button onclick="switchTab('cheatsheet')" id="tab-btn-cheatsheet" class="tab-btn px-3 py-1.5 rounded-lg transition-colors text-amber-300 hover:text-amber-100 flex items-center gap-1.5 font-bold">
          <i data-lucide="pen-tool" class="w-4 h-4 text-amber-400"></i> Handwritten Cheat Sheet
        </button>
      </nav>
    </div>
  </header>

  <!-- Main Container -->
  <main class="max-w-7xl mx-auto px-4 py-6 flex-1 w-full">

    <!-- ========================================== -->
    <!-- TAB 1: PRACTICE EXAM (MCQs & SHORT ANSWER) -->
    <!-- ========================================== -->
    <div id="tab-quiz" class="tab-content block">
      <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">
        <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-100 pb-4">
          <div>
            <h2 class="text-2xl font-bold text-slate-900">Randomized Practice Exam</h2>
            <p class="text-sm text-slate-500">Curated from all lecture slides: Architectural Design, System Modeling, UML, Testing & MC/DC, SDLC.</p>
          </div>
          <div class="flex items-center gap-3">
            <span id="score-counter" class="text-sm font-semibold bg-indigo-50 text-indigo-700 px-3 py-1.5 rounded-lg border border-indigo-100">
              Score: 0 / 0 (0%)
            </span>
            <button onclick="renderRandomQuiz(10)" class="bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 shadow-sm transition">
              <i data-lucide="shuffle" class="w-4 h-4"></i> Generate 10-Question Test
            </button>
            <button onclick="renderRandomQuiz(999)" class="bg-slate-200 hover:bg-slate-300 text-slate-700 text-sm font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition">
              Practice All Questions
            </button>
          </div>
        </div>
        <div id="quiz-container" class="space-y-6 mt-6">
          <!-- Dynamically populated -->
        </div>
      </div>
    </div>

    <!-- ==================================================== -->
    <!-- TAB 2: 8 IN-CLASS UML DIAGRAMS INTERACTIVE DRILLS     -->
    <!-- ==================================================== -->
    <div id="tab-uml" class="tab-content hidden">
      <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">
        <div class="border-b border-slate-100 pb-4 mb-6">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-2xl font-bold text-slate-900">The 8 In-Class UML Diagrams</h2>
              <p class="text-sm text-slate-500">Practice constructing the exact UML diagrams covered during lectures and in-class activities.</p>
            </div>
            <span class="bg-indigo-100 text-indigo-800 text-xs font-bold px-3 py-1 rounded-full border border-indigo-200">
              Exam Section B Focus
            </span>
          </div>
        </div>

        <!-- UML Drill Selector (8 In-Class Diagrams) -->
        <div class="flex flex-wrap gap-2 mb-6">
          <button onclick="showUmlDrill('hospital')" id="btn-drill-hospital" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 text-white">
            1. Hospital Class Diagram (3 Compartments)
          </button>
          <button onclick="showUmlDrill('bank')" id="btn-drill-bank" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            2. Bank Account & Realization
          </button>
          <button onclick="showUmlDrill('adapter')" id="btn-drill-adapter" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            3. Adapter Pattern Class Diagram
          </button>
          <button onclick="showUmlDrill('seqdoc')" id="btn-drill-seqdoc" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            4. Doctor Record Sequence (Alt & Loop)
          </button>
          <button onclick="showUmlDrill('seqmentcare')" id="btn-drill-seqmentcare" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            5. Mentcare View Info Sequence
          </button>
          <button onclick="showUmlDrill('insulin')" id="btn-drill-insulin" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            6. Insulin Pump Activity (Fork & Join)
          </button>
          <button onclick="showUmlDrill('swimlanes')" id="btn-drill-swimlanes" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            7. Activity Diagram with Swimlanes
          </button>
          <button onclick="showUmlDrill('microwave')" id="btn-drill-microwave" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            8. Microwave Oven State Machine
          </button>
          <button onclick="showUmlDrill('usecase')" id="btn-drill-usecase" class="uml-drill-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200">
            9. Use Case Diagram (Include vs Extend)
          </button>
        </div>

        <!-- DRILL 1: HOSPITAL CLASS DIAGRAM -->
        <div id="drill-hospital" class="uml-drill-view block">
          <div class="bg-slate-50 border-l-4 border-indigo-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 1: Hospital Management Class Diagram</h3>
            <p class="text-xs text-slate-600 mt-1">
              <strong>Rules:</strong> Always draw 3 compartments (Name, Attributes, Operations). Nouns = Classes, Noun phrases = Attributes, Verbs = Operations.<br>
              <strong>Scenario:</strong> Hospital has Departments. Department employs Doctors and maintains LabTests. If a Department closes, LabTests are destroyed, but Doctors keep their licenses and survive. MedicalRecord specializes into SurgicalRecord and OfficeVisitRecord.
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div class="uml-box shadow-sm">
              <div class="uml-header text-indigo-950 font-bold">Department</div>
              <div class="uml-section">- deptId: String<br>- name: String</div>
              <div class="uml-section">+ getDoctors(): List&lt;Doctor&gt;<br>+ scheduleTest(t: LabTest)</div>
            </div>

            <div class="uml-box shadow-md border-indigo-400 bg-indigo-50/20">
              <div class="uml-header bg-indigo-100 text-indigo-950 font-bold">
                <input id="u1-name" placeholder="Class Name? (e.g. Doctor)" class="w-full text-center font-bold bg-white border border-slate-300 rounded px-1 text-xs">
              </div>
              <div class="uml-section">
                <textarea id="u1-attr" placeholder="- doctorId: String&#10;- specialty: String" rows="2" class="w-full text-xs font-mono p-1 border border-slate-300 rounded"></textarea>
              </div>
              <div class="uml-section">
                <textarea id="u1-ops" placeholder="+ examinePatient()&#10;+ prescribeMedication()" rows="2" class="w-full text-xs font-mono p-1 border border-slate-300 rounded"></textarea>
              </div>
            </div>

            <div class="uml-box shadow-sm">
              <div class="uml-header text-indigo-950 font-bold">LabTest</div>
              <div class="uml-section">- testId: String<br>- resultData: String</div>
              <div class="uml-section">+ runAnalysis(): void<br>+ sendReport(): void</div>
            </div>
          </div>

          <!-- Relationship Choices -->
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-3 text-xs">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label class="font-semibold block mb-1">Department to Doctor Relationship:</label>
                <select id="rel-dept-doc" class="w-full p-2 border rounded bg-white">
                  <option value="">-- Choose Relationship --</option>
                  <option value="aggregation">Aggregation (&lt;&gt;-- open diamond at Department) - Doctor outlives Dept</option>
                  <option value="composition">Composition (&lt;*&gt;-- solid diamond at Department)</option>
                  <option value="generalization">Generalization (--|&gt; hollow triangle)</option>
                </select>
              </div>
              <div>
                <label class="font-semibold block mb-1">Department to LabTest Relationship:</label>
                <select id="rel-dept-lab" class="w-full p-2 border rounded bg-white">
                  <option value="">-- Choose Relationship --</option>
                  <option value="composition">Composition (&lt;*&gt;-- solid diamond at Department) - Tests destroyed with Dept</option>
                  <option value="aggregation">Aggregation (&lt;&gt;-- open diamond at Department)</option>
                  <option value="association">Simple Association (---)</option>
                </select>
              </div>
              <div>
                <label class="font-semibold block mb-1">MedicalRecord to SurgicalRecord:</label>
                <select id="rel-med-surg" class="w-full p-2 border rounded bg-white">
                  <option value="">-- Choose Relationship --</option>
                  <option value="generalization">Generalization (--|&gt; solid line with hollow triangle at MedicalRecord)</option>
                  <option value="realization">Realization (..|&gt; dashed line with hollow triangle)</option>
                  <option value="composition">Composition (&lt;*&gt;--)</option>
                </select>
              </div>
              <div>
                <label class="font-semibold block mb-1">Rule for classes with no methods:</label>
                <select id="rel-compartments" class="w-full p-2 border rounded bg-white">
                  <option value="">-- Choose Answer --</option>
                  <option value="three">Must always draw all 3 compartments, leaving the 3rd compartment empty</option>
                  <option value="two">Draw only 2 compartments</option>
                </select>
              </div>
            </div>
            <button onclick="checkHospitalDrill()" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-lg text-xs">Verify Diagram 1</button>
            <div id="hospital-feedback" class="mt-2 text-xs font-semibold"></div>
          </div>
        </div>

        <!-- DRILL 2: BANK ACCOUNT & REALIZATION -->
        <div id="drill-bank" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-blue-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 2: Bank Account Hierarchy & Interface Realization</h3>
            <p class="text-xs text-slate-600 mt-1">
              <code>BankAccount</code> is an abstract parent class. <code>SavingsAccount</code> implements the <code>InterestBearing</code> interface. <code>Customer</code> owns an <code>Address</code>.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-3 text-xs">
            <div>
              <p class="font-bold text-slate-800 mb-1">1. How is an abstract class name denoted in UML?</p>
              <label class="block"><input type="radio" name="bank-q1" value="italic"> Italic font style or tagged with &laquo;abstract&raquo;</label>
              <label class="block"><input type="radio" name="bank-q1" value="bold"> Bold underlined font</label>
            </div>
            <div>
              <p class="font-bold text-slate-800 mb-1">2. Which connector denotes Realization (implements interface)?</p>
              <label class="block"><input type="radio" name="bank-q2" value="realization"> Dashed line with hollow triangle pointing to Interface (<code>..|&gt;</code>)</label>
              <label class="block"><input type="radio" name="bank-q2" value="generalization"> Solid line with hollow triangle pointing to parent (<code>--|&gt;</code>)</label>
            </div>
            <div>
              <p class="font-bold text-slate-800 mb-1">3. Customer to Address relationship:</p>
              <label class="block"><input type="radio" name="bank-q3" value="composition"> Composition (&lt;*&gt; solid diamond at Customer - Address lifecycle bound)</label>
              <label class="block"><input type="radio" name="bank-q3" value="aggregation"> Aggregation (&lt;&gt; hollow diamond)</label>
            </div>
            <button onclick="checkBankDrill()" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-lg text-xs">Verify Diagram 2</button>
            <div id="bank-feedback" class="mt-2 text-xs font-semibold"></div>
          </div>
        </div>

        <!-- DRILL 3: ADAPTER PATTERN CLASS DIAGRAM -->
        <div id="drill-adapter" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-emerald-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 3: Adapter Design Pattern Class Diagram (In-Class Activity)</h3>
            <p class="text-xs text-slate-600 mt-1">
              Converts the interface of a class (Adaptee) into another interface that clients expect.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-3 text-xs">
            <div>
              <p class="font-bold text-slate-800 mb-1">1. In the Object Adapter pattern, what connects the `Adapter` to the `Adaptee`?</p>
              <select id="ad-q1" class="w-full p-2 border rounded bg-white">
                <option value="">-- Choose Relationship --</option>
                <option value="correct">Association / Composition: Adapter holds a private reference to the Adaptee instance (adaptee.specificRequest())</option>
                <option value="wrong1">Inheritance only</option>
                <option value="wrong2">Dependency injection without reference</option>
              </select>
            </div>
            <div>
              <p class="font-bold text-slate-800 mb-1">2. What connects `Adapter` to the `Target` interface?</p>
              <select id="ad-q2" class="w-full p-2 border rounded bg-white">
                <option value="">-- Choose Relationship --</option>
                <option value="correct">Realization: Adapter implements the Target interface (`..|> Target`)</option>
                <option value="wrong1">Generalization from abstract class only</option>
              </select>
            </div>
            <div>
              <p class="font-bold text-slate-800 mb-1">3. What does `Client` interact with?</p>
              <select id="ad-q3" class="w-full p-2 border rounded bg-white">
                <option value="">-- Choose Target --</option>
                <option value="correct">The Target interface directly (remains decoupled from Adaptee implementation)</option>
                <option value="wrong1">The Adaptee directly</option>
              </select>
            </div>
            <button onclick="checkAdapterDrill()" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-lg text-xs">Verify Diagram 3</button>
            <div id="ad-fb" class="mt-2 text-xs font-semibold"></div>
          </div>
        </div>

        <!-- DRILL 4: SEQUENCE DIAGRAM (ALT & LOOP) -->
        <div id="drill-seqdoc" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-purple-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 4: Doctor Viewing Record Sequence Diagram (Fragments: Alt & Loop)</h3>
            <p class="text-xs text-slate-600 mt-1">
              Doctor queries patient surgical record. If authorized (`[isAuthorized]`), loop over lab tests and return results; else return error.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-3 text-xs">
            <div class="space-y-2">
              <p>Combined Fragment Matching:</p>
              <div class="p-2 border bg-white rounded">
                alt fragment: Represents if-then-else alternatives. Separated by a dashed horizontal line with boolean guards in square brackets [authorized] and [else].
              </div>
              <div class="p-2 border bg-white rounded">
                loop fragment: Represents repeated execution (e.g. iterating over test records) with guard condition [hasMoreTests] or range [1, *].
              </div>
              <div class="p-2 border bg-white rounded">
                Arrowhead Types: Synchronous calls use a solid line with filled arrowhead (--&blacktriangleright;). Return messages use a dashed line with stick arrowhead (&lt;- - -).
              </div>
            </div>
          </div>
        </div>

        <!-- DRILL 5: MENTCARE VIEW INFO SEQUENCE -->
        <div id="drill-seqmentcare" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-sky-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 5: Mentcare View Patient Info Sequence Diagram</h3>
            <p class="text-xs text-slate-600 mt-1">
              Actor &rarr; UI/Boundary &rarr; Controller &rarr; Entity/Database.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-3 text-xs">
            <p class="font-bold text-slate-800">Identify the correct message sequence from lecture:</p>
            <div class="space-y-1 font-mono text-[11px] bg-white p-3 border rounded">
              1. Receptionist --&blacktriangleright; :PatientUI : viewInfo(patientId)<br>
              2. :PatientUI --&blacktriangleright; :PatientController : getDetails(patientId)<br>
              3. :PatientController --&blacktriangleright; :PatientDatabase : query(patientId)<br>
              4. :PatientDatabase &lt;- - - :PatientController : return record<br>
              5. :PatientUI &lt;- - - :Receptionist : display patient details
            </div>
          </div>
        </div>

        <!-- DRILL 6: INSULIN PUMP ACTIVITY -->
        <div id="drill-insulin" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-amber-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 6: Insulin Pump Activity Diagram (Fork & Join)</h3>
            <p class="text-xs text-slate-600 mt-1">
              A Fork bar splits 1 incoming flow into multiple concurrent parallel flows. A Join bar synchronizes concurrent parallel flows into 1 outgoing flow.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-2 text-xs">
            <div class="p-3 bg-white border rounded">
              &bull; Fork: After sensor measures blood sugar, execution splits into: (1) Compute required insulin dosage, and (2) Log sensor timestamp.<br>
              &bull; Join: Both the dosage calculation and logging must complete before advancing to Inject Insulin.<br>
              &bull; Decision Diamond: [sugarLevel &gt; safeRange] &rarr; Inject Insulin; [sugarLevel &le; safeRange] &rarr; Sleep 10 min.
            </div>
          </div>
        </div>

        <!-- DRILL 7: SWIMLANES ACTIVITY -->
        <div id="drill-swimlanes" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-teal-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 7: Activity Diagram with Swimlanes (Partitions)</h3>
            <p class="text-xs text-slate-600 mt-1">
              Partitions (swimlanes) designate which organizational role or system component is responsible for executing each activity.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-2 text-xs">
            <div class="p-3 bg-white border rounded">
              &bull; Lane 1 (Patient/User): Submit appointment request, Provide insurance card.<br>
              &bull; Lane 2 (Receptionist): Verify identity, Check doctor schedule, Confirm slot.<br>
              &bull; Lane 3 (Medical Records Subsystem): Generate appointment record, update patient history.<br>
              &bull; Transitions crossing lanes: Indicate handoff of responsibility between actors/systems.
            </div>
          </div>
        </div>

        <!-- DRILL 8: MICROWAVE STATE MACHINE -->
        <div id="drill-microwave" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-rose-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 8: Microwave Oven State Machine Diagram</h3>
            <p class="text-xs text-slate-600 mt-1">
              UML State Transition Syntax: Event [Guard] / Action
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-2 text-xs">
            <div class="p-3 bg-white border rounded">
              &bull; States: Waiting, Half power, Full power, Set time, Operation, Disabled.<br>
              &bull; Transition example: start [door_closed] / run_generator(300W)<br>
              &bull; Door open event: From state Operation &rarr; door_open / stop_generator(), turn_lamp_on() &rarr; state Disabled.
            </div>
          </div>
        </div>

        <!-- DRILL 9: USE CASE DIAGRAM -->
        <div id="drill-usecase" class="uml-drill-view hidden">
          <div class="bg-slate-50 border-l-4 border-indigo-600 p-4 rounded-r-lg mb-6">
            <h3 class="font-bold text-slate-900 text-sm">Diagram 9: Use Case Diagram (Include vs Extend)</h3>
            <p class="text-xs text-slate-600 mt-1">
              Differentiating mandatory sub-tasks from optional extension points.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-2 text-xs">
            <div class="p-3 bg-white border rounded">
              &bull; &laquo;include&raquo;: Mandatory sub-routine. Base use case is incomplete without it. Dashed arrow points from base use case to included use case. (E.g. View Record --&gt; &laquo;include&raquo; --&gt; Authenticate User).<br>
              &bull; &laquo;extend&raquo;: Optional behavior triggered under specific conditions at an extension point. Base is complete on its own. Dashed arrow points from extending use case to base use case. (E.g. Print Hardcopy --&gt; &laquo;extend&raquo; --&gt; View Record).
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 3: ARCHITECTURE MODELS                -->
    <!-- ========================================== -->
    <div id="tab-architecture" class="tab-content hidden">
      <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">
        <div class="border-b border-slate-100 pb-4 mb-4">
          <h2 class="text-2xl font-bold text-slate-900">Architecture Design Models</h2>
          <p class="text-sm text-slate-500">Core architectural patterns: Layered, Repository, Client-Server, Pipe & Filter, and Control Models.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <div class="p-4 border rounded-lg bg-slate-50">
            <h3 class="font-bold text-slate-800 text-sm mb-1">1. Mentcare Layered System (Slide 54)</h3>
            <p>Layer 1: Web browser</p>
            <p>Layer 2: Login, Role checking, Form & menu manager, Data validation</p>
            <p>Layer 3: Security mgmt, Patient info manager, Data import/export, Report generation</p>
            <p>Layer 4: Transaction management, Patient database</p>
          </div>
          <div class="p-4 border rounded-lg bg-slate-50">
            <h3 class="font-bold text-slate-800 text-sm mb-1">2. IDE Repository Model (Slide 31)</h3>
            <p>Center: Project Information & Code</p>
            <p>Surrounding: Model Editor, Code Generator, Java Editor, Python Editor, Report Generator, Design Analyzer, Design Translator</p>
          </div>
          <div class="p-4 border rounded-lg bg-slate-50">
            <h3 class="font-bold text-slate-800 text-sm mb-1">3. Film Library Client-Server (Slide 34)</h3>
            <p>Clients 1-4 &harr; Wide-bandwidth network &harr; Catalogue, Video, Picture, Hypertext servers</p>
          </div>
          <div class="p-4 border rounded-lg bg-slate-50">
            <h3 class="font-bold text-slate-800 text-sm mb-1">4. Customer Invoicing Pipe & Filter (Slide 38)</h3>
            <p>Invoices &rarr; [Process Invoices] &rarr; [Identify Payments] &rarr; [Issue Receipts] (Receipts) & [Find Payments Due] &rarr; [Issue Reminder] (Reminders)</p>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: 5 TEST CASES MATRIX BUILDER        -->
    <!-- ========================================== -->
    <div id="tab-testcases" class="tab-content hidden">
      <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">
        <div class="border-b border-slate-100 pb-4 mb-4 flex justify-between items-center">
          <div>
            <h2 class="text-2xl font-bold text-slate-900">Section B: 5 Test Cases Practice Matrix</h2>
            <p class="text-sm text-slate-500">Practice constructing complete test cases with objectives, pre-conditions, inputs, expected results, and pass/fail criteria.</p>
          </div>
          <button onclick="fillExampleTestCases()" class="text-xs bg-slate-100 hover:bg-slate-200 font-semibold text-slate-700 px-3 py-1.5 rounded border border-slate-300">
            Load Model Solution
          </button>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs border border-slate-300 rounded-lg">
            <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-300">
              <tr>
                <th class="p-2 border-r border-slate-300 w-16">TC ID</th>
                <th class="p-2 border-r border-slate-300 w-44">Test Objective / Category</th>
                <th class="p-2 border-r border-slate-300 w-44">Pre-Conditions</th>
                <th class="p-2 border-r border-slate-300">Test Steps & Inputs</th>
                <th class="p-2 border-r border-slate-300">Expected Result</th>
                <th class="p-2 w-32">Pass/Fail Criteria</th>
              </tr>
            </thead>
            <tbody id="test-case-rows" class="divide-y divide-slate-200">
              <!-- Dynamically populated rows 1 to 5 -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 5: PRINTABLE CHEAT SHEET (GOOD DOG PLAIN FONT, PURE UNBOLDED)     -->
    <!-- ============================================================== -->
    <div id="tab-cheatsheet" class="tab-content hidden">
      <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">
        
        <!-- Screen Top Bar -->
        <div class="flex flex-wrap justify-between items-center border-b border-slate-200 pb-4 mb-4 no-print gap-3">
          <div>
            <h2 class="text-xl font-bold text-slate-900">Handwritten Cheat Sheet (Good Dog Plain Font)</h2>
            <p class="text-xs text-slate-500 mt-0.5">
              Custom installed GoodDog Plain font • Organic micro-variations • Pure unbolded text • Zero lines & zero headers
            </p>
          </div>
          <button onclick="window.print()" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-5 py-2.5 rounded-lg flex items-center gap-2 shadow-sm transition text-xs sm:text-sm">
            <i data-lucide="printer" class="w-4 h-4"></i> Print Cheat Sheet
          </button>
        </div>

        <!-- ============================================== -->
        <!-- PRINT AREA: GOOD DOG PLAIN HANDWRITTEN NOTES     -->
        <!-- ============================================== -->
        <div id="cheat-sheet-print-area" class="font-pure-notes text-slate-900 leading-snug">
          
          <!-- ============================== -->
          <!-- SIDE 1: FRONT OF PAGE          -->
          <!-- ============================== -->
          <div class="p-1 mb-4">
            
            <!-- Dense Organic Unstructured Cram Streams -->
            <div class="hw-stream-side1">
              
              <!-- Column 1 -->
              <div>
                <div class="hw-blob hw-b-1">sdlc & fundamentals: reqs -> design -> code -> test -> deploy -> maint. 4 p's: people, product, process, project. 4 attributes of good software: maintainability (system evolves w/ customer needs), dependability & security (reliable, safe, resilient), efficiency (optimal cpu, memory, response time), acceptability (understandable, usable, compatible). cost breakdown: roughly 60% dev cost, 40% testing cost; for custom software, long-term evolution costs exceed original development! acm/ieee ethics priority: 1.public interest 2.client & employer 3.product 4.judgment 5.management 6.profession 7.colleagues 8.self.</div>
                <div class="hw-blob hw-b-2">requirements & use cases: functional = services system must provide & reactions to inputs. non-functional (nfr) = constraints on services (timing, security, standards, reliability, portability). testability rule: avoid subjective vague words (instantaneously, user-friendly, rapidly, little training) -> must rewrite into measurable numbers (e.g. response <= 200 ms, training time <= 2 hours, errors <= 1 per 8 hour shift). use cases: <<include>> = mandatory subroutine (base incomplete without it); <<extend>> = optional behavior triggered at extension point (base is complete on its own).</div>
                <div class="hw-blob hw-b-3">kruchten 4+1 view model: logical view = end-user functionality, domain abstractions, classes, entities (audience: dev/user, concern: functional reqs). process view = dynamic runtime behavior, concurrency, processes, threads, synchronization, rpc/message bus (audience: dev, concern: performance & scalability). development view = static organization of code, packages, modules, libraries, build hierarchy (audience: dev, concern: reuse & ease of build). physical view = hardware topology, execution nodes, network interconnects, distribution across processors (audience: sys eng/ops, concern: quality attributes). +1 scenarios (use cases) = unifies and links the other 4 views together, validating architecture against all requirements.</div>
              </div>

              <!-- Column 2 -->
              <div>
                <div class="hw-blob hw-b-4">architecture & patterns: ieee definition: fundamental organization of a system embodied in its components, relationships to one another and environment, and principles governing design and evolution. partitioning: 1.system structuring -> 2.control modeling -> 3.modular decomposition. why plan: stakeholder communication, system analysis before code, large-scale reuse, security access boundary enforcement. layered architecture: hierarchical layers where layer n only depends on n-1; pros: replaceable layers if interfaces constant, changes localized to adjacent layers, multi-layer security defense; cons: clean separation hard in practice, performance overhead passing calls through layers. repository: central passive data store accessed and updated by independent active subsystems (example: ide w/ project info and code surrounded by java editor, python editor, code gen, report gen); pros: efficient sharing of large data, independent components; cons: single point of failure and bottleneck, data evolution difficult. client-server: dedicated servers offering services across network to clients (film library: catalogue server, video server, picture server); pros: distributed failure isolation, straightforward scaling; cons: network latency, each server a failure point. pipe & filter: sequential stream transformations (unix pipes, customer invoicing: invoices -> process invoices -> identify payments -> issue receipts); pros: subsystem reuse, intuitive; cons: agreed data format overhead, parsing latency. mvc: controller handles input -> updates model -> view renders display.</div>
                <div class="hw-blob hw-b-5">system control models: centralized call-return model = top-down subroutine call tree for sequential code (main -> subsystems -> methods). centralized manager model = single process controls stopping, starting, and coordination of concurrent processes (controller coordinating sensors, actuators, computation, fault handler, ui). decentralized broadcast model = events published to common message bus; registered subsystems handle events (effective for distributed systems, but sender does not know if or when event handled). decentralized interrupt-driven model = hardware interrupt array mapped to specific memory locations; dedicated handlers watch address and coordinate response (temperature, radiation, fire alarm, fuel handlers; used for fast real-time response, but complex to program and hard to validate).</div>
              </div>

              <!-- Column 3 -->
              <div>
                <div class="hw-blob hw-b-6">software testing fundamentals: verification = "are we building the product right?" (conformance to specification). validation = "are we building the right product?" (satisfies customer operational needs). dijkstra's axiom: "program testing can be used to show the presence of bugs, but never to show their absence!" defect testing exposes flaws; validation testing demonstrates system meets user requirements. v-model lifecycle pairings: requirements engineering <-> acceptance testing (alpha and beta); system specification <-> system testing; architectural design <-> subsystem and integration testing; detailed module design <-> unit testing.</div>
                <div class="hw-blob hw-b-7">test scaffolding & junit: test driver = software module that invokes unit under test and passes simulated inputs. test stub / mock = dummy module called by unit under test that returns synthetic values. test harness = framework automating execution of test suites (example: junit). test oracle = mechanism determining if actual output matches expected output. junit annotations: @Test = marks executable test method; @Before / @BeforeEach = executes before every individual test method (fixture init); @After / @AfterEach = executes after every test method (fixture teardown); @BeforeClass / @BeforeAll = static, executes once before all tests in class (opens db/sockets); @AfterClass / @AfterAll = static, executes once after all tests finish (closes db/sockets).</div>
                <div class="hw-blob hw-b-8">mentcare & atm architecture: mentcare 4-layer system: layer 1 is web browser; layer 2 is user communications (login, role checking, form & menu manager, data validation); layer 3 is information retrieval and modification (security management, patient info manager, data import/export, report generation); layer 4 is transaction management and patient database. atm 4-tier pipeline: i/o processing <-> application logic <-> transaction manager <-> database. atm 3-phase flow: input (get account id, validate card, select service) -> process (query account, update account) -> output (print details, return card, dispense cash).</div>
              </div>

            </div>
          </div>

          <!-- PAGE BREAK FOR DOUBLE SIDED -->
          <div class="page-break"></div>

          <!-- ============================== -->
          <!-- SIDE 2: BACK OF PAGE           -->
          <!-- ============================== -->
          <div class="p-1">
            
            <!-- Dense Organic Unstructured Cram Streams -->
            <div class="hw-stream-side2">
              
              <!-- Column 1 -->
              <div>
                <div class="hw-blob hw-b-9">uml class diagrams: strict 3-compartment rule: every class box must show all 3 compartments: 1.class name 2.attributes 3.operations (even if attributes or operations are empty, draw the 3rd compartment box line!). class discovery: nouns become classes, noun phrases become attributes, verbs become operations. abstract class: render name in italic font style or tag with <<abstract>>. visibility symbols: + is public, - is private, # is protected, - is package-private. attribute format: visibility name : type = default-val. operation format: visibility name(parameter : type) : returnType. association: solid line without arrows or with open navigation arrow; multiplicity placed at both ends (1, 0..1, 1..*, *). aggregation (<>--): open hollow diamond at whole end ("has-a", weak containment, part can exist independently of whole: department <>-- doctor). composition (<*>--): solid filled diamond at whole end ("part-of", strong containment, part lifetime bound to whole; destroyed when whole deleted: department <*>-- labtest, customer <*>-- address). generalization (--/->): solid line with hollow triangular arrowhead pointing to parent ("is-a", inheritance: medicalrecord --/-> surgicalrecord, bankaccount --/-> checkingaccount). realization (../->): dashed line with hollow triangular arrowhead pointing to interface (savingsaccount ../-> interestbearing). dependency (..>): dashed line with open arrow ("uses").</div>
                <div class="hw-blob hw-b-10">adapter pattern: client calls methods on target interface; target = abstract interface expected by client; adapter = implements target interface (../-> target) and holds private reference to adaptee instance (adapter calls adaptee.specificRequest()); adaptee = existing legacy class with incompatible interface that client cannot call directly.</div>
                <div class="hw-blob hw-b-11">sequence diagrams: lifeline = vertical dashed line extending downward from object box; activation bar = thin vertical rectangle on lifeline indicating execution control; synchronous call = solid line with filled arrowhead (----->); sender halts until reply; asynchronous call = solid line with stick open arrowhead (--->); sender continues without waiting; reply / return message = dashed line with stick open arrow (<---); object creation = message labeled <<create>> points directly to object box; object destruction = an x placed at base of an activation lifeline. combined fragments: alt = mutually exclusive if-then-else separated by dashed line with [guard]; opt = optional conditional execution if only; loop [min, max] = repetition over elements; par = concurrent parallel sub-sequences.</div>
              </div>

              <!-- Column 2 -->
              <div>
                <div class="hw-blob hw-b-12">activity & statechart diagrams: activity elements: initial node = solid filled circle; activity state = rounded rectangle; decision and merge = diamond symbols with [guard]; fork bar = thick black synchronization bar splitting 1 incoming flow into 2 or more concurrent parallel flows; join bar = thick black synchronization bar waiting for multiple concurrent flows to finish before 1 outgoing flow proceeds; final node = bullseye (solid circle inside outer circle); swimlanes (partitions) = indicate which role or subsystem performs each activity. insulin pump flow: sensor measures blood sugar -> fork bar splits into: (1) calculate required insulin dosage, and (2) log sensor reading -> join bar synchronizes both -> decision diamond [sugar > target] -> inject insulin. state machine: states = rounded rectangles (waiting, half power, full power, operation, disabled); initial state = solid black circle; final state = bullseye; transition label syntax: event [guard] / action (example: start [door-closed] / run-generator(300w); door-open / stop-generator(), turn-lamp-on() -> state disabled).</div>
                <div class="hw-blob hw-b-13">white-box structural testing: statement coverage (c0) = percentage of executable statements traversed by test cases (statements executed / total statements * 100%; weakest metric! cannot detect missing false branches in single if). branch coverage (c1) = requires every decision branch (both true and false edges in control flow graph) traversed at least once. subsumption rule: branch coverage subsumes statement coverage (100% branch implies 100% statement, but not vice-versa!). condition coverage = requires each individual boolean sub-condition in composite expression to evaluate to true and false at least once. mc/dc (modified condition/decision coverage) = required by do-178c avionics safety standard: each condition must be shown to independently affect overall decision outcome while holding all other conditions fixed; for n conditions, requires n + 1 test cases (compared to 2**n for multiple condition coverage). path coverage = every possible execution path from entry to exit tested (often infinite or intractable due to loops). loop boundary = test 0 iterations, 1 iteration, typical iterations, max-1 iterations, max iterations.</div>
              </div>

              <!-- Column 3 -->
              <div>
                <div class="hw-blob hw-b-14">black-box testing (ep & bva): equivalence partitioning (ep) = divide input domain into valid and invalid equivalence classes; select 1 representative test input per class. boundary value analysis (bva) = test values immediately at, below, and above boundary edges: min-1, min, min+1, nominal, max-1, max, max+1. pin [0000..9999]: valid class = 1234; invalid classes = negative numbers (-1), numbers > 9999 (10000), non-digits ("abcd"), 3 digits, 5 digits.</div>
                <div class="hw-blob hw-b-15">5 test cases structure & rubric: format: [tc id, objective, pre-conditions, test steps/inputs, expected result, pass/fail criteria]. tc-01 (valid ep registration): pre: user logged in; inputs: valid name, dob, ssn; expected: patient record created in db, unique id assigned, http 201 toast; criteria: record persists in db. tc-02 (min boundary value): inputs: age = 0 (minimum valid age); expected: form accepted, classified as infant; criteria: profile created with infant tag. tc-03 (negative boundary value): inputs: age = -1; expected: submission blocked, error message "age must be >= 0" displayed; criteria: no db write, form retains input. tc-04 (concurrency / double withdrawal): pre: balance = $100; inputs: simultaneous atm and mobile app withdrawals of $100 within 10 ms; expected: 1st transaction succeeds, 2nd rejected for insufficient funds; criteria: balance never negative ($0 balance). tc-05 (exception / null pointer): inputs: doctorid = null on prescription request; expected: system rejects with http 400 bad request, logs missing doctor reference safely; criteria: no unhandled 500 crash or stack trace shown.</div>
                <div class="hw-blob hw-b-16">relational database & normalization: entity integrity: primary key (pk) column cannot be null and must be unique. referential integrity: foreign key (fk) column must match an existing valid pk value in parent table or be null. 1nf (first normal form): all column values must be atomic (no repeating groups, multi-valued attributes, or composite values). 2nf (second normal form): table is in 1nf and every non-key attribute is fully functionally dependent on the entire composite primary key (no partial key dependencies). 3nf (third normal form): table is in 2nf and no non-key attribute depends on another non-key attribute (no transitive dependencies). canonical rule: "every attribute must depend on the key, the whole key, and nothing but the key!"</div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="bg-slate-900 text-slate-400 text-xs py-4 text-center border-t border-slate-800 no-print">
    <p>Software Engineering CSC 4350/6350 • Exam 3 Study Suite • Tailored for Dr. Tushara Sadasivuni</p>
  </footer>

  <!-- Interactive Logic -->
  <script>
    // Tab Switching
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('bg-indigo-600', 'text-white');
        btn.classList.add('text-indigo-200');
      });

      document.getElementById('tab-' + tabId).classList.remove('hidden');
      const activeBtn = document.getElementById('tab-btn-' + tabId);
      if (activeBtn) {
        activeBtn.classList.remove('text-indigo-200');
        activeBtn.classList.add('bg-indigo-600', 'text-white');
      }
      lucide.createIcons();
    }

    // UML Drill Sub-views
    function showUmlDrill(drillId) {
      document.querySelectorAll('.uml-drill-view').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.uml-drill-btn').forEach(b => {
        b.classList.remove('bg-indigo-600', 'text-white');
        b.classList.add('bg-slate-100', 'text-slate-700');
      });

      document.getElementById('drill-' + drillId).classList.remove('hidden');
      const activeBtn = document.getElementById('btn-drill-' + drillId);
      if (activeBtn) {
        activeBtn.classList.remove('bg-slate-100', 'text-slate-700');
        activeBtn.classList.add('bg-indigo-600', 'text-white');
      }
    }

    // Verification Logic for UML Drills
    function checkHospitalDrill() {
      const r1 = document.getElementById('rel-dept-doc').value;
      const r2 = document.getElementById('rel-dept-lab').value;
      const r3 = document.getElementById('rel-med-surg').value;
      const r4 = document.getElementById('rel-compartments').value;
      const fb = document.getElementById('hospital-feedback');

      let correct = (r1 === 'aggregation') && (r2 === 'composition') && (r3 === 'generalization') && (r4 === 'three');

      if (correct) {
        fb.className = "mt-2 text-xs font-semibold text-emerald-700";
        fb.innerHTML = "✅ Correct! Department-to-Doctor is Aggregation (Doctor outlives Department). Department-to-LabTest is Composition (tests destroyed). MedicalRecord is Generalization. And class boxes always have 3 compartments.";
      } else {
        fb.className = "mt-2 text-xs font-semibold text-rose-700";
        fb.innerHTML = "❌ Check: Doctors survive hospital closure (Aggregation), but LabTests do not (Composition). And always draw 3 compartments.";
      }
    }

    function checkBankDrill() {
      const q1 = document.querySelector('input[name="bank-q1"]:checked')?.value;
      const q2 = document.querySelector('input[name="bank-q2"]:checked')?.value;
      const q3 = document.querySelector('input[name="bank-q3"]:checked')?.value;
      const fb = document.getElementById('bank-feedback');

      if (q1 === 'italic' && q2 === 'realization' && q3 === 'composition') {
        fb.className = "mt-2 text-xs font-semibold text-emerald-700";
        fb.innerHTML = "✅ Correct! Abstract classes are italicized, interfaces are realized with dashed hollow arrows, and Customer-Address is composition.";
      } else {
        fb.className = "mt-2 text-xs font-semibold text-rose-700";
        fb.innerHTML = "❌ Incorrect. Check abstract notation (italicized) and interface realization (dashed line with hollow triangle).";
      }
    }

    function checkAdapterDrill() {
      const q1 = document.getElementById('ad-q1').value;
      const q2 = document.getElementById('ad-q2').value;
      const q3 = document.getElementById('ad-q3').value;
      const fb = document.getElementById('ad-fb');

      if (q1 === 'correct' && q2 === 'correct' && q3 === 'correct') {
        fb.className = "mt-2 text-xs font-semibold text-emerald-700";
        fb.innerHTML = "✅ 100% Correct Adapter Pattern: Client calls Target; Adapter implements Target and wraps Adaptee via private reference!";
      } else {
        fb.className = "mt-2 text-xs font-semibold text-rose-700";
        fb.innerHTML = "❌ Check your answers against the in-class Adapter activity.";
      }
    }

    // Comprehensive Questions Database from all lecture slides
    const ALL_QUESTIONS = [
      {
        q: "What is the IEEE definition of software architecture?",
        options: [
          "The fundamental organization of a system, embodied in its components, their relationships to one another and the environment, and the principles governing its design and evolution.",
          "The detailed class diagrams and database schema required for code implementation.",
          "The high-level user interface mockups presented to the client.",
          "The hardware topology consisting of cloud servers, microprocessors, and network switches."
        ],
        answer: 0,
        explanation: "Slide 9 quotes the exact IEEE Definition of Software Architecture."
      },
      {
        q: "In Kruchten's 4+1 View Model of software architecture, which view addresses concurrency, performance, and scalability?",
        options: [
          "Process View",
          "Logical View",
          "Physical View",
          "Development View"
        ],
        answer: 0,
        explanation: "The Process View deals with dynamic runtime threads, concurrency, and performance (Slide 20). Logical view deals with domain functionality."
      },
      {
        q: "In Kruchten's 4+1 View Model, what is the role of the '+1' (Use Case Scenarios)?",
        options: [
          "It unifies and links the elements of the other 4 views together.",
          "It is an optional view only used for web applications.",
          "It replaces the physical hardware deployment model.",
          "It is used exclusively by database administrators."
        ],
        answer: 0,
        explanation: "Slide 16 notes that Use Case Scenarios unify and link the elements of the other 4 views, ensuring completeness with respect to requirements."
      },
      {
        q: "Drawing a class with only 2 compartments when it has no operations is:",
        options: [
          "Wrong! You must always draw all 3 compartments, leaving the operations compartment empty.",
          "Acceptable, as empty compartments can be omitted.",
          "Standard UML best practice.",
          "Required by IEEE 830."
        ],
        answer: 0,
        explanation: "Class boxes must always show all 3 compartments: Name, Attributes, Operations."
      },
      {
        q: "In the hospital management scenario, why is the relationship between Department and Doctor modeled as Aggregation (<>--) rather than Composition (<*>--)?",
        options: [
          "Because doctors possess independent licenses and continue to exist if the department closes.",
          "Because doctors cannot exist without a department.",
          "Because doctors inherit all methods from the Department.",
          "Because aggregation is faster to implement in Java."
        ],
        answer: 0,
        explanation: "Aggregation is weak containment: the part (Doctor) outlives the whole (Department). Composition is strong containment where parts are destroyed with the whole."
      },
      {
        q: "What is the primary architectural weakness of the Repository (Blackboard) architecture style?",
        options: [
          "The repository is a single point of failure and can easily become a communication bottleneck.",
          "Components cannot share large datasets.",
          "Data format changes are isolated and never affect tools.",
          "It cannot be used with databases."
        ],
        answer: 0,
        explanation: "Central passive repositories create a single point of failure; if the repository crashes or slows down, all dependent tools halt (Slide 32)."
      },
      {
        q: "Which architectural style is best illustrated by Unix command-line pipes such as 'cat file.txt | cut -d, -f2 | sort | uniq -c'?",
        options: [
          "Pipe and Filter Architecture",
          "Layered Model",
          "Shared Repository Model",
          "Client-Server Architecture"
        ],
        answer: 0,
        explanation: "Slide 36 uses the exact Unix command line pipeline to illustrate the Pipe and Filter architecture."
      },
      {
        q: "In system control modeling, what is the key difference between the Call-Return model and the Manager model?",
        options: [
          "Call-Return applies to sequential systems (top-down subroutine tree); Manager model applies to concurrent systems.",
          "Call-Return is decentralized; Manager model is event-driven.",
          "Call-Return requires hardware interrupts; Manager does not.",
          "Manager model cannot handle user interfaces."
        ],
        answer: 0,
        explanation: "Slides 42 & 43: Call-Return is top-down for sequential systems; Manager model is for concurrent systems where one process coordinates others."
      },
      {
        q: "In the Mentcare layered architecture (Slide 54), what constitutes Layer 2 (User Communications / Interface Management)?",
        options: [
          "Login, Role checking, Form and menu manager, Data validation",
          "Web browser and HTML UI only",
          "Patient Database and Transaction Management",
          "Security management and Report generation"
        ],
        answer: 0,
        explanation: "Slide 54: Layer 2 contains Login, Role checking, Form and menu manager, and Data validation."
      },
      {
        q: "Which testing coverage metric guarantees that every decision statement evaluates to both TRUE and FALSE at least once?",
        options: [
          "Branch (Decision) Coverage",
          "Statement Coverage",
          "Condition Coverage",
          "Function Coverage"
        ],
        answer: 0,
        explanation: "Branch coverage (C1) requires every decision branch (both True and False edges in the Control Flow Graph) to be traversed at least once. It subsumes statement coverage."
      },
      {
        q: "What is Edsger Dijkstra's famous axiom regarding software testing?",
        options: [
          "Program testing can be used to show the presence of bugs, but never to show their absence.",
          "A program that passes all test cases is proven error-free.",
          "Testing is 100% effective when branch coverage reaches 100%.",
          "Verification proves correctness; validation proves efficiency."
        ],
        answer: 0,
        explanation: "Testing demonstrates defects exist; passing all tests only proves no defects were discovered by those specific test cases."
      },
      {
        q: "In white-box testing, how does Modified Condition/Decision Coverage (MC/DC) reduce testing cost compared to Multiple Condition Coverage?",
        options: [
          "It tests each condition independently affecting the outcome, requiring only n + 1 tests instead of 2^n tests.",
          "It skips all negative conditions.",
          "It requires only 2 tests regardless of the number of conditions.",
          "It ignores composite boolean expressions."
        ],
        answer: 0,
        explanation: "For n boolean conditions, Multiple Condition Coverage requires 2^n test cases, while MC/DC requires only n + 1 test cases while proving independent effect."
      },
      {
        q: "Which JUnit annotation designates a fixture method that must run ONCE before any of the test methods in the test class execute?",
        options: [
          "@BeforeClass (JUnit 4) / @BeforeAll (JUnit 5)",
          "@Before / @BeforeEach",
          "@TestSetup",
          "@ClassRule"
        ],
        answer: 0,
        explanation: "@BeforeClass (or @BeforeAll) executes once before any test methods, typically used to open expensive database connections or servers."
      },
      {
        q: "What is the difference between a Test Driver and a Test Stub?",
        options: [
          "A Driver simulates the calling component above the unit; a Stub simulates a called sub-component below the unit.",
          "A Driver simulates a database; a Stub simulates the operating system.",
          "A Driver runs assertions; a Stub generates random inputs.",
          "A Driver is used in black-box testing; a Stub is used in acceptance testing."
        ],
        answer: 0,
        explanation: "In scaffolding: Test Drivers simulate higher-level callers to invoke the method under test; Test Stubs replace unfinished lower-level modules called by the unit."
      },
      {
        q: "Which normalization stage eliminates partial functional dependencies on a composite primary key?",
        options: [
          "Second Normal Form (2NF)",
          "First Normal Form (1NF)",
          "Third Normal Form (3NF)",
          "Boyce-Codd Normal Form (BCNF)"
        ],
        answer: 0,
        explanation: "1NF removes repeating groups. 2NF requires 1NF AND that every non-prime attribute is fully functionally dependent on the entire primary key."
      }
    ];

    let currentQuiz = [];
    let userAnswers = {};

    function renderRandomQuiz(count) {
      userAnswers = {};
      let shuffled = [...ALL_QUESTIONS].sort(() => 0.5 - Math.random());
      currentQuiz = count >= shuffled.length ? shuffled : shuffled.slice(0, count);

      const container = document.getElementById('quiz-container');
      container.innerHTML = '';

      currentQuiz.forEach((item, idx) => {
        const qCard = document.createElement('div');
        qCard.className = "p-5 border border-slate-200 rounded-xl bg-slate-50/50 hover:bg-white transition";

        let optionsHtml = item.options.map((opt, optIdx) => `
          <label class="flex items-start gap-3 p-2.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 cursor-pointer text-xs mb-2 transition">
            <input type="radio" name="q_${idx}" value="${optIdx}" onchange="selectQuizAnswer(${idx}, ${optIdx})" class="mt-0.5 text-indigo-600 focus:ring-indigo-500">
            <span class="text-slate-700">${opt}</span>
          </label>
        `);

        qCard.innerHTML = `
          <div class="flex items-start justify-between gap-4 mb-3">
            <span class="text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-md">Question ${idx + 1}</span>
          </div>
          <p class="text-sm font-semibold text-slate-900 mb-4">${item.q}</p>
          <div class="space-y-1">${optionsHtml.join('')}</div>
          <div id="q_feedback_${idx}" class="mt-3 text-xs hidden"></div>
        `;
        container.appendChild(qCard);
      });

      updateScoreBadge();
      lucide.createIcons();
    }

    function selectQuizAnswer(qIdx, optIdx) {
      userAnswers[qIdx] = optIdx;
      const q = currentQuiz[qIdx];
      const fb = document.getElementById(`q_feedback_${qIdx}`);
      fb.classList.remove('hidden');

      if (optIdx === q.answer) {
        fb.className = "mt-3 p-3 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-medium";
        fb.innerHTML = `✅ <strong>Correct!</strong> ${q.explanation}`;
      } else {
        fb.className = "mt-3 p-3 rounded-lg bg-slate-100 border border-slate-300 text-slate-800 text-xs font-medium";
        fb.innerHTML = `❌ <strong>Incorrect.</strong> Correct answer: <em>${q.options[q.answer]}</em><br><span class="text-slate-600 mt-1 block">${q.explanation}</span>`;
      }
      updateScoreBadge();
    }

    function updateScoreBadge() {
      const answeredKeys = Object.keys(userAnswers);
      const totalAnswered = answeredKeys.length;
      let correctCount = 0;
      answeredKeys.forEach(k => {
        if (userAnswers[k] === currentQuiz[k].answer) correctCount++;
      });
      const pct = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
      document.getElementById('score-counter').innerText = `Score: ${correctCount} / ${totalAnswered} (${pct}%)`;
    }

    // Populate Test Cases Matrix
    function initTestCaseRows() {
      const tbody = document.getElementById('test-case-rows');
      tbody.innerHTML = '';
      for (let i = 1; i <= 5; i++) {
        tbody.innerHTML += `
          <tr class="hover:bg-slate-50">
            <td class="p-2 font-mono font-bold text-indigo-700 border-r border-slate-300">TC-0${i}</td>
            <td class="p-2 border-r border-slate-300"><input id="tc-obj-${i}" class="w-full p-1 border rounded" placeholder="Objective (e.g., Boundary Valid Age)"></td>
            <td class="p-2 border-r border-slate-300"><input id="tc-pre-${i}" class="w-full p-1 border rounded" placeholder="Pre-condition (e.g., User logged in)"></td>
            <td class="p-2 border-r border-slate-300"><textarea id="tc-steps-${i}" class="w-full p-1 border rounded" rows="2" placeholder="Inputs (e.g., Age = 18)"></textarea></td>
            <td class="p-2 border-r border-slate-300"><textarea id="tc-exp-${i}" class="w-full p-1 border rounded" rows="2" placeholder="Expected result (e.g., Account created)"></textarea></td>
            <td class="p-2"><input id="tc-pass-${i}" class="w-full p-1 border rounded" placeholder="Criteria (e.g., HTTP 201 Created)"></td>
          </tr>
        `;
      }
    }

    function fillExampleTestCases() {
      const examples = [
        { obj: "Valid Patient Registration (Equivalence: Valid)", pre: "User logged in as Receptionist", steps: "Enter name 'John Doe', DOB '1990-05-12', valid SSN, click Save", exp: "Patient profile saved to DB with unique PatientID; Success toast shown", pass: "PatientID generated & HTTP 201" },
        { obj: "Boundary Value Analysis (Min Age Boundary)", pre: "Registration form open", steps: "Enter age = 0 (boundary minimum permitted age)", exp: "Form accepted, patient classified as 'Infant'", pass: "Profile created with Infant tag" },
        { obj: "Negative Test (Invalid PIN Boundary)", pre: "ATM card inserted, PIN prompt displayed", steps: "Input 3-digit PIN '123' and press Enter", exp: "Input blocked or error message 'PIN must be 4 digits' displayed", pass: "Transaction denied, card retained or reprompted" },
        { obj: "Concurrency / Double Withdrawal", pre: "Account balance = $100", steps: "Simultaneous ATM and mobile app withdrawals of $100 triggered within 10ms", exp: "First request completes; second request rejected for insufficient funds", pass: "Balance never becomes negative ($0 balance)" },
        { obj: "Exception / Null Pointer Handling", pre: "Medical record service running", steps: "Submit prescription request with DoctorID = NULL", exp: "System rejects with 400 Bad Request; logs 'Missing Doctor Reference' safely", pass: "No unhandled stack trace or 500 crash" }
      ];

      examples.forEach((ex, idx) => {
        let i = idx + 1;
        document.getElementById(`tc-obj-${i}`).value = ex.obj;
        document.getElementById(`tc-pre-${i}`).value = ex.pre;
        document.getElementById(`tc-steps-${i}`).value = ex.steps;
        document.getElementById(`tc-exp-${i}`).value = ex.exp;
        document.getElementById(`tc-pass-${i}`).value = ex.pass;
      });
    }

    // Initialize on page load
    window.onload = function() {
      renderRandomQuiz(10);
      initTestCaseRows();
      lucide.createIcons();
    };
  </script>
</body>
</html>
"""

html_out = template.replace('__B64_FONT__', b64_font)

with open(r'c:\Users\jamal\Documents\~~~Software engineering\SWE-Exam-3\index.html', 'w', encoding='utf-8') as out:
    out.write(html_out)

print("index.html written successfully!")
