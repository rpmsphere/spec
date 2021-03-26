%define pkg_name StepIntoChinese

Name:		stepintochinese
Version:        0.6
Release:        1
Summary:        Step Into Chinese is a flexible language-mining tool to assist English speakers seeking to understand Chinese language.
Group:          Educations/Games
License:        LGPL
URL:            https://wiki.mozilla.org/Special:Search?search=i18n&go=Go
Source0:        http://www.asymptopia.org/filemgmt_data/files/%{pkg_name}-%{version}.tgz
Requires:       python2, pygame
BuildArch:	noarch

%description
Step Into Chinese is a flexible language-mining tool to assist English speakers seeking to understand Chinese language. The lack of a one-to-one correspondence between Chinese characters and the corresponding Pinyin is often regarded as the greatest difficulty facing learners of Chinese. Step Into Chinese has been designed to address exactly this difficulty.

Inside is an extensively cross-referenced data structure which allows the user to pursue deeper understanding of contexts, for example, by "locking on" to a particular Pinyin context and viewing successive instances of the same morpheme used in similar contexts.

The user can also "lock on" to English words in the Pinyin translations, English words in the collective phrase translations, and even unicode strings used to represent Chinese characters in either traditional or simplified representations. Frequency information relative to the number of occurances of each Pinyin morpheme, in each context throughout the data structure, is displayed for each entry.

Flashcards can be created/deleted by F5/F6 keys at any time, and the flashcards, themselves, can be displayed in four different styles.

The application data structure contains over 26,000 modern Chinese words and concepts, corresponding to over 8,300 separate Chinese characters. Colors are used consistently throughout the application for rapid location and absorption of information. Most colors, dimensions and images can be changed through the simple graphical configuration interface. The user interface is keyboard driven, using only the common keys: F1-F12, Home, End, Enter, Backspace, and the arrow keys. A heads-up display showing a color-coded standard keyboard map is readily available for quick key reference. The mouse wheel provides an additional way to scroll through entries. The full set of features are demonstrated in the following animated demo/tutorial. 

%prep
%setup -q -n %{pkg_name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0644 -p sic.ico  $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{pkg_name}
Name[zh_TW]=漸進式中文教學
Comment=Step Into Chinese is a flexible language-mining tool to assist English speakers seeking to understand Chinese language.
Comment[zh_TW]=Step Into Chinese 讓外國人學習中文的軟體，可以從英文單子中，找出中文的意思。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;
EOF

#Exec
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
python2 StepIntoChinese.py
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*/*.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuild for Fedora
* Mon Dec 08 2008 Feather Mountain <john@ossii.com.tw> 0.6-1.ossii
- Build for OSSII
