Name:           jbook
Version:        1.4
Release:        1
Summary:        A Tool For Reading Electronic Texts
Group:          Applications/Education
License:        GPL
URL:            https://jbook.sourceforge.net/
Source0:        https://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}-sources.tgz
Source1:        %{name}.png
BuildRequires:  java-devel
Requires:       jre
BuildArch:      noarch

%description
Project Gutenberg supplies a large number of free electronic texts. The JBook
project lets users retrieve, read, and bookmark electronic texts, primarily from
Project Gutenberg but eventually from other sources. The major goals are to:
 * Make etext reading easier
 * Promote literacy and reading
 * Advance the cause of Project Gutenberg 

%prep
%setup -q -n %{name}-%{version}-sources

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp *.class *.lst $RPM_BUILD_ROOT%{_datadir}/%{name}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images
cp images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=電子書閱讀機
Comment=A Tool For Reading Electronic Texts
Comment[zh_TW]=一套用來閱讀電子書的工具，可線上自動下載很多電子書。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;
EOF

#Exec
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF

cd %{_datadir}/%{name}
java -cp . JBook
EOF

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Fri Mar 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Fri Dec 5 2008 Feather Mountain <john@ossii.com.tw> 1.4-1
- Build for OSSII
