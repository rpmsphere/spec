Name: gtimer
Summary: GTK-based X11 task timer
Version: 2.0.0
Release: 1
Group: utils
License: Free Software
URL: https://www.k5n.us/gtimer.php
Source0: %{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: libX11-devel

%description
A graphical program that tracks how your time is spent.  Maintains a
simple list of tasks, each of which can belong to a project, and allows
you to track time in each.  Multiple clocks can run simultaneously,
annotations can be added to a day's time, and reports can be generated
in either HTML or text.  If GTimer detects that you're idle, you are
given the option of subtracting off the time you spent idle when you
return.

Compared to other time tracking applications, GTimer is graphical without
depending on a desktop environment and aims for simplicity rather than
attempting to be a full-fledged project tracking and billing application.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -Dm644 %{name}.1 %{buildroot}%{_datadir}/man/man1/%{name}.1

%files
%doc LICENSE COPYING AUTHORS NEWS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/man/man1/%{name}.1.*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuilt for Fedora
