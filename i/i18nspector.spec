%global _python_bytecompile_errors_terminate_build 0

Name:           i18nspector
Version:        0.27.1
Release:        1
Summary:        Tool for Checking gettext POT/PO/MO Files
License:        MIT
Group:          Development/Tools/Other
URL:            http://jwilk.net/software/i18nspector
Source0:        https://bitbucket.org/jwilk/i18nspector/downloads/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel
#BuildRequires:  python3-nose
BuildArch:      noarch

%description
i18nspector is a tool for checking translation templates (POT), message
catalogues (PO) and compiled message catalogues (MO) files for common
problems. These files are used by the GNU gettext translation functions
and tools in many different development environments.

Checks include: incorrect or inconsistent character encoding, missing
headers, incorrect language codes and improper plural forms.

%prep
%setup -q

%build
make

%install
%make_install PREFIX=%{_prefix}

%files
%doc doc/{changelog,tags.txt,todo,README,LICENSE}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%doc %{_mandir}/man?/*

%changelog
* Sun Nov 13 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.27.1
- Rebuilt for Fedora
* Mon Dec  9 2013 lazy.kent@opensuse.org
- Update to 0.13.1.
  * Fix test failures with Python 3.4.
  * Fix stripping delay annotations from terminfo capabilities.
  * Improve the test suite.
* Sat Sep 14 2013 lazy.kent@opensuse.org
- Update to 0.13.
  * Summary of tag changes:
    + Added:
  - conflicting-message-flags
  - duplicate-message-flag
  - invalid-range-flag
  - range-flag-without-plural-string
  - redundant-message-flag
  - unknown-message-flag
  * Check for duplicate, conflicting, redundant, or unknown message
    flags.
  * Strip leading and trailing spaces from flag lines.
  * Be verbose when checking for messages with empty msgid with
    source code references.
  * Reduce duplicate-flag-for-header-entry severity to minor.
  * Check for zero width no-break space (U+FEFF) in translations
    and header entries.
  * Improve the test suite.
  * Work around a trailing comment parsing bug in polib.
    https://bitbucket.org/izi/polib/issue/51
* Tue Jul 30 2013 lazy.kent@opensuse.org
- Update to 0.12.
  * Summary of tag changes:
    + Added:
  - boilerplate-in-date
  * Don't emit empty-file for MO files with only system-dependent
    messages, or with minor revision greater than 1.
  * Don't emit no-package-name-in-project-id-version if the package
    name consists of only non-ASCII letters.
  * Fix parsing some atypical PO comments.
  * Parse more date formats.
  * Check for xgettext boilerplate in dates.
  * Strip trailing whitespace when parsing header entry.
  * Allow only tabs and spaces between “nplurals=…” and “plural=…”.
  * Remove Bihari (codes “bh”, “bih”) from the data files; it's not
    a single language, but a language collection.
  * Implement 8-bit encodings without iconv(3) or iconv(1).
  * Add “SEE ALSO” section to the manual page.
  * Improve the test suite.
  * Improve the makefile.
* Mon Jun 24 2013 lazy.kent@opensuse.org
- Update to 0.11.1.
  * Fix the MO file parser:
    + Detect encoding by inspecting only the first message with
    empty msgid.
    + Fix compatibility with Python 3.3.
  * Use the custom MO file encoding detection method rather than
    the provided by polib.
- Changes in 0.11.
  * Summary of tag changes:
    + Added:
  - distant-header-entry
  - duplicate-flag-for-header-entry
  - duplicate-header-entry
  - duplicate-header-field-x-poedit
  - empty-msgid-message-with-plural-forms
  - empty-msgid-message-with-source-code-references
  - unexpected-flag-for-header-entry
  - unusual-character-in-header-entry
  * Fix letter codes for tags with severity important.
  * Reduce severity of arithmetic-error-in-unused-plural-forms,
    codomain-error-in-unused-plural-forms, and
    incorrect-unused-plural-forms to normal.
  * Implement custom header parser for PO files, and custom MO file
    parser.
  * Check for duplicate header entries.
  * Check for unusually located header entries.
  * Overhaul handling of duplicates and stray lines in the header
    entry.
    + Emit duplicate-header-field-x-poedit (instead of the generic
    duplicate-header-field) for duplicate X-Poedit-Language and
    X-Poedit-Country headers fields.
  * Work around a flag parsing bug in polib.
  * Check for duplicate and unexpected flags for header entries.
  * Check for unusual characters in header entries.
  * Check for messages with empty msgid (header entries?) with
    source code references or plural forms.
  * Fix some false-positive language-disparity when PO basename
    does not designate translation language.
  * Fix the no-report-msgid-bugs-to-header-field description.
  * Fix a few typos in the tag descriptions.
  * Improve the test suite.
    + Add new tests.
    + Use a dedicated nose plugin for blackbox tests.
* Sat Jun 15 2013 lazy.kent@opensuse.org
- Update to 0.10.
  * Summary of tag changes:
    + Added:
  - boilerplate-in-content-type
  - conflict-marker-in-header-entry
  - conflict-marker-in-translation
  - duplicate-header-field-content-transfer-encoding
  - duplicate-header-field-content-type
  - duplicate-header-field-date
  - duplicate-header-field-language
  - duplicate-header-field-language-team
  - duplicate-header-field-last-translator
  - duplicate-header-field-mime-version
  - duplicate-header-field-plural-forms
  - duplicate-header-field-project-id-version
  - duplicate-header-field-report-msgid-bugs-to
  - fuzzy-header-entry
  * Check for boilerplate (“charset=CHARSET”) in the Content-Type
    header field.
  * Check header field name syntax.
  * Overhaul duplicate header field detection.
    + Emit duplicate-header-field only for non-standard fields.
    Downgrade duplicate-header-field to minor/wild-guess.
    + Emit duplicate-header-field-$NAME for standard fields.
    + Don't trust values of standard header fields if duplicates
    exist.
  * Check for conflict markers (“#-#-#-#-#  …  #-#-#-#-#”).
  * Check for fuzzy header entries.
  * Fix a typo in the language-team-equal-to-last-translator
    description.
  * Post-process the manual page, so that it can be more easily
    translated by po4a.
  * If iconv(3) is available in the C standard library, use it to
    implement encodings that are not implemented in the Python
    standard library.
  * Don't pass -s to iconv(1); it makes GNU iconv quieten errors,
    and other implementations don't have this option at all.
  * Improve the test suite:
    + Add new tests.
    + Make exception messages raised when a subprocess fails more
    readable.
    + Make it possible to use a custom Python interpreter for “make
    test”.
* Sun Jun  9 2013 lazy.kent@opensuse.org
- Update to 0.9.2.
  * When emitting broken-encoding, don't output the whole file, but
    only the undecodable bytes in a small context.
* Sat Jun  1 2013 lazy.kent@opensuse.org
- Correct source URL.
- Correct build dependencies.
* Sat May 25 2013 lazy.kent@opensuse.org
- Update to 0.9.1.
  * Brown paper bag release.
  * Don't complain about leading/trailing newlines in fuzzy
    messages.
  * Improve the test suite.
- Changes in 0.9.
  * Summary of tag changes:
    + Added:
  - inconsistent-leading-newlines
  - inconsistent-trailing-newlines
  * Check for inconsistent leading/trailing newlines in messages.
  * Check for unusual characters also in plural translations.
  * Add information about version and date to the manual page.
  * Fix stripping delay annotations from terminfo capabilities.
- Changes in 0.8.3.
  * Improve the test suite.
    + Skip some tests when run with (pseudo-)root privileges.
  * Add “test” target to Makefile.
  * Recognize “PROJECT VERSION” as boilerplate in the
    Project-Id-Version header field.
- Drop i18nspector-0.8.2-run_tests.patch (fixed upstream).
* Wed May  1 2013 lazy.kent@opensuse.org
- Run test suite (add i18nspector-0.8.2-run_tests.patch: add "test"
  target to Makefile; BuildRequires: python3-curses, python3-nose,
  python3-polib).
* Thu Apr 18 2013 lazy.kent@opensuse.org
- Update to 0.8.2.
  * Make it possible to declare that a language has more than one
    correct Plural-Forms.
  * Add plural forms information for the following languages:
    Belarusian, Bosnian, Croatian, Hungarian, Russian, Serbian,
    Turkish, Ukrainian.
  * Improve the test suite.
* Thu Feb 28 2013 lazy.kent@opensuse.org
- Update to 0.8.1.
  * Improve the documentation.
  * Remove an incorrect assertion in the plural expression parser.
* Sun Feb 17 2013 lazy.kent@opensuse.org
- Requires python3 for openSUSE < 12.3.
* Wed Feb  6 2013 lazy.kent@opensuse.org
- Initial package created - 0.8.
