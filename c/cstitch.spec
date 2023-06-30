%undefine _debugsource_packages

Name:		cstitch
Summary:	A free and open source program for creating cross stitch patterns from images
Version:	0.9.8
Release:	8.1
License:	GPLv2+
Group:		Applications/Graphics
URL:		https://cstitch.sourceforge.net/
Source0:	%{name}_%{version}_code.zip
Source1:        https://sourceforge.net/projects/cstitch/files/Cstitch/Icons/icons.zip
BuildRequires:	qt5-qtbase-devel
BuildRequires:	python2

%description
Convert images to cross stitch patterns: choose the number of colors to use
and the final pattern size; edit your pattern (save and restore your work);
save your pattern as a pdf.

%prep
%setup -q -n %{name}_%{version}
unzip %{SOURCE1} -d icons

%build
doc/createDocs.py
qmake-qt5 -project
./progen.py
qmake-qt5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -Dm755 %{name}_%{version} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 icons/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%clean
rm -rf %{buildroot}

%files
%doc README* LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Wed Aug 22 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.8
- Rebuilt for Fedora
