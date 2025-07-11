Name: language-pack-sinitic
Summary: Translations for some sinitic languages
Version: 2025.07
Release: 1
License: Open Source
Group: Translations
URL: https://github.com/chinese-opendesktop/%{name}
Source0: https://github.com/chinese-opendesktop/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: msghack
BuildRequires: translate-toolkit
BuildRequires: qt5-linguist
BuildRequires: msgchi >= 1.4
BuildRequires: uni2ascii
BuildArch: noarch

%description
Translation data for all supported packages for some sinitic languages.

%package -n language-pack-cmn
Summary: Translations for Mandarin Chinese
Requires: glibc-langpack-cmn

%description -n language-pack-cmn
Translation data for all supported packages for Mandarin Chinese.

%package -n language-pack-yue
Summary: Translations for Yue Chinese
Requires: glibc-langpack-yue

%description -n language-pack-yue
Translation data for all supported packages for Yue Chinese.

%prep
%setup -q

%build
make

%install
%make_install

%files -n language-pack-cmn
%{_datadir}/locale/cmn*/LC_MESSAGES/*.mo
%{_libdir}/R/library/translations/cmn*/LC_MESSAGES/*.mo
%{_libdir}/R/library/*/po/cmn*/LC_MESSAGES/*.mo
%{_libdir}/textadept/core/locales/locale.cmn*.conf
%{_datadir}/*/*/cmn*.po
%{_datadir}/FBReader/resources/cmn*.xml
%{_datadir}/Telegram/Desktop_cmn*.strings
%{_datadir}/locale/cmn*/LC_MESSAGES/*.qm
%{_datadir}/*/*cmn*.qm
%{_datadir}/*/*/*cmn*.qm
%{_datadir}/*/*/*/*cmn*.qm
%{_datadir}/*/*/*/*/*cmn*.qm
%{_libexecdir}/*/Translations/*cmn*.qm
%{_datadir}/zlibrary/resources/cmn*.xml
%{_datadir}/childsplay_sp/*/*/words-cmn*
%{_datadir}/*/*/cmn*/LC_MESSAGES/*.mo
%{_datadir}/liblunar/holiday.dat-cmn*
%{_datadir}/logo/logolib/Messages.cmn*
/var/www/html/clipbucket/includes/langs/cmn*.lang
/etc/joe/joerc.cmn*
%{python3_sitelib}/openshot_qt/language/OpenShot.cmn*.qm
/usr/lib/mcm/i18n/locale/cmn*/LC_MESSAGES/mcm.mo
%{_libdir}/doublecmd/language/doublecmd.cmn*.po
%{_libdir}/libreoffice/program/resource/cmn*/LC_MESSAGES/*.mo
%{_libdir}/viewmol/locale/cmn*/LC_MESSAGES/Viewmol.mo
%{_datadir}/cobras/cobras_cmn*.ts
%{_datadir}/discwrapper/po/cmn*/discwrapper.mo
%{_datadir}/easymp3gain/lang/easymp3gain.cmn*.po
%{_datadir}/exe/locale/cmn*/exe_cmn*.po
%{_datadir}/lazpaint/i18n/lazpaint.cmn*.po
%{_datadir}/leechcraft/qml5/cpuload/ts/leechcraft_cpuload_qml_cmn*.ts
%{_datadir}/leechcraft/qml5/lemon/ts/leechcraft_lemon_qml_cmn*.ts
%{_datadir}/locale/applets/LC_MESSAGES/universal-cmn*.mo
%{_datadir}/locale/cmn*/cups_cmn*.po
%{_datadir}/locale/cmn*/gutenprint_cmn*.po
%{_datadir}/locale/manager/LC_MESSAGES/screenlets-cmn*.mo
%{_datadir}/locale/pyspread/po/cmn*.po
%{_datadir}/meandmyshadow/data/locale/cmn*.po
%{_datadir}/qaquarelle/locale/cmn*/qaquarelle.qm
%{_datadir}/qmetro/locale/cmn*.lng
%{_datadir}/ufo2000/translations/ufo2000-cmn*.po
%{_datadir}/ulipad/lang/cmn*/ulipad_cmn*.mo
%{_datadir}/wazapp/i18n/cmn*.ts
%{_datadir}/wikidpad/WikidPad_cmn*.po
%{_datadir}/winff/languages/winff.cmn*.po
%{_datadir}/lenmus/*/locale/cmn*/*_cmn*.mo
%{_datadir}/*/*/*/*_cmn*.properties
%{_libdir}/*/*/*/*_cmn*.properties
%{_datadir}/*/*/*_cmn*.properties
%{_datadir}/*/chrome/locale/branding/cmn*/brand.properties
%{_datadir}/azardi/chrome/locale/cmn*/azardi2.properties
%{_datadir}/pebl/battery/SNARC/translations/cmn*.txt
/lib/python3.*/site-packages/*/*/cmn*/LC_MESSAGES/*.mo
/lib/python3.*/site-packages/*/*/*/cmn*/LC_MESSAGES/*.mo
%{_libdir}/python2.*/site-packages/Editra/locale/cmn*/LC_MESSAGES/Editra.mo
%{_libdir}/*/*/*_cmn*.qm
%{_datadir}/PrusaSlicer/localization/cmn*/PrusaSlicer.mo
%{_datadir}/lucidor/chrome/locale/cmn*/*.properties
%{_datadir}/skychart/data/language/skychart.cmn*.po
%{_datadir}/texlive/tlpkg/translations/cmn*.po
%{_datadir}/*/*/*/cmn*/LC_MESSAGES/*.mo
/opt/wemeet/bin/*_cmn*.qm

%files -n language-pack-yue
%{_datadir}/locale/yue*/LC_MESSAGES/*.mo
%{_libdir}/R/library/translations/yue*/LC_MESSAGES/*.mo
%{_libdir}/R/library/*/po/yue*/LC_MESSAGES/*.mo
%{_libdir}/textadept/core/locales/locale.yue*.conf
%{_datadir}/*/*/yue*.po
%{_datadir}/FBReader/resources/yue*.xml
%{_datadir}/Telegram/Desktop_yue*.strings
%{_datadir}/locale/yue*/LC_MESSAGES/*.qm
%{_datadir}/*/*yue*.qm
%{_datadir}/*/*/*yue*.qm
%{_datadir}/*/*/*/*yue*.qm
%{_datadir}/*/*/*/*/*yue*.qm
%{_libexecdir}/*/Translations/*yue*.qm
%{_datadir}/zlibrary/resources/yue*.xml
%{_datadir}/childsplay_sp/*/*/words-yue*
%{_datadir}/*/*/yue*/LC_MESSAGES/*.mo
%{_datadir}/liblunar/holiday.dat-yue*
%{_datadir}/logo/logolib/Messages.yue*
/var/www/html/clipbucket/includes/langs/yue*.lang
/etc/joe/joerc.yue*
%{python3_sitelib}/openshot_qt/language/OpenShot.yue*.qm
/usr/lib/mcm/i18n/locale/yue*/LC_MESSAGES/mcm.mo
%{_libdir}/doublecmd/language/doublecmd.yue*.po
%{_libdir}/libreoffice/program/resource/yue*/LC_MESSAGES/*.mo
%{_libdir}/viewmol/locale/yue*/LC_MESSAGES/Viewmol.mo
%{_datadir}/cobras/cobras_yue*.ts
%{_datadir}/discwrapper/po/yue*/discwrapper.mo
%{_datadir}/easymp3gain/lang/easymp3gain.yue*.po
%{_datadir}/exe/locale/yue*/exe_yue*.po
%{_datadir}/lazpaint/i18n/lazpaint.yue*.po
%{_datadir}/leechcraft/qml5/cpuload/ts/leechcraft_cpuload_qml_yue*.ts
%{_datadir}/leechcraft/qml5/lemon/ts/leechcraft_lemon_qml_yue*.ts
%{_datadir}/locale/applets/LC_MESSAGES/universal-yue*.mo
%{_datadir}/locale/yue*/cups_yue*.po
%{_datadir}/locale/yue*/gutenprint_yue*.po
%{_datadir}/locale/manager/LC_MESSAGES/screenlets-yue*.mo
%{_datadir}/locale/pyspread/po/yue*.po
%{_datadir}/meandmyshadow/data/locale/yue*.po
%{_datadir}/qaquarelle/locale/yue*/qaquarelle.qm
%{_datadir}/qmetro/locale/yue*.lng
%{_datadir}/ufo2000/translations/ufo2000-yue*.po
%{_datadir}/ulipad/lang/yue*/ulipad_yue*.mo
%{_datadir}/wazapp/i18n/yue*.ts
%{_datadir}/wikidpad/WikidPad_yue*.po
%{_datadir}/winff/languages/winff.yue*.po
%{_datadir}/lenmus/*/locale/yue*/*_yue*.mo
%{_datadir}/*/*/*/*_yue*.properties
%{_libdir}/*/*/*/*_yue*.properties
%{_datadir}/*/*/*_yue*.properties
%{_datadir}/*/chrome/locale/branding/yue*/brand.properties
%{_datadir}/azardi/chrome/locale/yue*/azardi2.properties
%{_datadir}/pebl/battery/SNARC/translations/yue*.txt
/lib/python3.*/site-packages/*/*/yue*/LC_MESSAGES/*.mo
/lib/python3.*/site-packages/*/*/*/yue*/LC_MESSAGES/*.mo
%{_libdir}/python2.*/site-packages/Editra/locale/yue*/LC_MESSAGES/Editra.mo
%{_libdir}/*/*/*_yue*.qm
%{_datadir}/PrusaSlicer/localization/yue*/PrusaSlicer.mo
%{_datadir}/lucidor/chrome/locale/yue*/*.properties
%{_datadir}/skychart/data/language/skychart.yue*.po
%{_datadir}/texlive/tlpkg/translations/yue*.po
%{_datadir}/*/*/*/yue*/LC_MESSAGES/*.mo
/opt/wemeet/bin/*_yue*.qm

%clean
rm -rf %{buildroot}

%changelog
* Thu Jul 10 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 2025.07
- Rebuilt for Fedora
