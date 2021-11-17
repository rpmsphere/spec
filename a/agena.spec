Summary: The Agena Programming Language
Name: agena
Version: 2.22.1
Release: 1
License: MIT
Group: Development/Language
URL: http://agena.sourceforge.net/
Source0: http://downloads.sourceforge.net/agena/%{name}-%{version}-src.tar.gz

%description
Agena is an easy-to-learn procedural programming language designed to be used
in science, scripting, and many other applications.

%prep
%setup -q -n %{name}-%{version}-src

%build
bash makealllinux.sh

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc licence change.log
%{_bindir}/%{name}

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.22.1
- Rebuilt for Fedora
