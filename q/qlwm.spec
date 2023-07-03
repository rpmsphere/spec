%undefine _debugsource_packages

Name:               qlwm
Version:            4.3
Release:            4.1
Summary:            A Qt based window manager 
Source0:            https://www.alinden.mynetcologne.de/qlwm/qlwm-4.3.tar.gz
URL:                https://www.alinden.mynetcologne.de/qlwm/
Group:              System/GUI/Other
License:            GNU General Public License version 3 (GPL v3)
BuildRequires:      qt4-devel
Patch0:             qlwm-pol51.patch

%description
qlwm is yet another window manager for the X11 system. Because it makes heavy
use of a high level API it can be kept small, stable and easy to maintain.
One of the design rules was to get a non-intrusive environment that does not
bother the user with unnecessary details or features while providing comfort
and high functionality.

%prep
%setup -q
%patch0 -p1

%build
export SUBLIBS="-lX11 -lXext"
make %{?_smp_flags}

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -m755 src/qlwm dclock/dclock mail/biff %{buildroot}%{_libexecdir}/%{name}
install -Dm644 qlwm.1 %{buildroot}%{_mandir}/man1/qlwm.1
cp -a files %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s ../libexec/qlwm/qlwm %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc README
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Mar 14 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3
- Rebuilt for Fedora
