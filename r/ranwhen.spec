%global checkout 20130428git6d8cac6

Name:           ranwhen
Version:        1
Release:        3.1
Summary:        Visualize when your system was running
Group:          Applications/System
License:        GPLv3+
URL:            https://github.com/p-e-w/%{name}
Source0:        %{name}-%{version}-%{checkout}.tar.gz
#Source0-generating script
Source1:        %{name}-get-snapshot.sh
Requires:       python3
BuildArch:      noarch

%description
Ranwhen is a python script that graphically shows
in your terminal when your system was running in the past.

%prep
%setup -q -n %{name}-%{version}-%{checkout}

%build

%install
install -Dm755 %{name}.py %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Tue May 28 2013 Simone Sclavi <darkhado@gmail.com> 1-1.20130428git6d8cac6
- Initial build
