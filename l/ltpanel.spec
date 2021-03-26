Name: ltpanel
Summary: Lightweight tasklist panel for minimalist WMs
Version: 0.2
Release: 6.1
License: GPL
Group: x11
URL: http://ltpanel.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: libX11-devel
BuildRequires: libXpm-devel

%description
ltpanel is a lightweight window list for the X Window System, similar
to GNOME's window list applet. It has been tested on IceWM and fvwm.
It should work with any GNOME-compliant Window Manager and is based
on Peter Zelezny's fspanel.

%prep
%setup -q

%build
make -C src

%install
install -Dm755 src/lpanel %{buildroot}%{_bindir}/%{name}
install -Dm644 doc/lpanel.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING* README* HISTORY
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Jan 03 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
