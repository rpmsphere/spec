%global debug_package %{nil}

Name: beebeep
Summary: Secure Network Chat
Version: 5.4.2
Release: 5.1
Group: Applications/Communications
URL: http://sourceforge.net/projects/beebeep/
Source0: https://sourceforge.net/projects/beebeep/files/Sources/%{name}-code-%{version}.zip
License: Qt Public License
BuildRequires: qt5-devel

%description
BeeBEEP is a secure network chat. You can talk and send files with all your
friends inside a local area network such of an office, home or internet cafe
without a server.

%prep
%setup -q -n %{name}-code-r1047

%build
qmake-qt5 -recursive
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mv test/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_libdir}
cp -a test/* %{buildroot}%{_libdir}

%files
%doc *.txt
%{_bindir}/%{name}
%{_libdir}/lib*

%changelog
* Mon Aug 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 5.4.2
- Rebuild for Fedora
