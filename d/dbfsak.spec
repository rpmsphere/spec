%undefine _debugsource_packages

Name: dbfsak
Summary: DBF Swiss Army Knife
Version: 4.5
Release: 5.1
Group: Applications/Databases
License: Artistic License
URL: https://dbfsak.sourceforge.net/
Source0: https://sourceforge.net/projects/dbfsak/files/%{name}-%{version}.src.tar.gz

%description
DBFSAK is a command line program designed to extract data from DBF
(dBase, FoxPro, Clipper, xBase) files. It can also be used to create
DBF files and populate them from your data.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README CREDITS CHANGES ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5
- Rebuilt for Fedora
