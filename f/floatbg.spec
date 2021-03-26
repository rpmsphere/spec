%global debug_package %{nil}

Name: floatbg
Summary: Slowly modify the color of the X root window
Version: 1.0
Release: 30.1
Group: x11
License: Free Software
Source0: %{name}_%{version}.orig.tar.gz
Patch0: floatbg_1.0-28.diff.gz
BuildRequires: imake
BuildRequires: libXext-devel

%description
Subtly changes the color of the root window over time, so slowly
that it won't be noticed. This is a good alternative to placing a
picture in the root window.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p 1

%build
xmkmf -a
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -Dm644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu May 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
