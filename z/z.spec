Name:           z
Version:        1.11
Release:        1
Summary:        Jump around
License:        opensource
URL:            https://github.com/rupa/z/
Source0:        %{name}-%{version}.tar.gz
BuildArch:  	noarch  

%description
Tracks your most used directories, based on frecency.
After a short learning phase, z will take you to the most frecent
directory that matches ALL of the regexes given on the command line.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README
%{_sysconfdir}/profile.d/%{name}.sh
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Oct 08 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
