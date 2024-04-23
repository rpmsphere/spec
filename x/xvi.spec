%undefine _debugsource_packages

Name: xvi
Summary: Small multiple-window version of the `vi' text editor
Version: 2.51
Release: 1
Group: editors
License: Free Software
URL: https://github.com/martinwguy/xvi
Source0: https://martinwguy.github.io/xvi/download/%{name}-%{version}.tar.gz

%description
xvi is the smallest clone of the famous "vi" editor, with almost all of the
commands of the original version by Bill Joy with the addition of a
multiple buffer feature which allows you to edit several files simultaneously
as well as allowing several views onto one file.

It does not implement the command-line "ex mode" and "open mode" of vi,
nor the smart programming-language-specific modes. Exact differences between
xvi and standard "vi" are listed in its manual page.

In spite of its name, it is not specific to the X Window System, and
and runs on any regular text terminal.

xvi was written by Chris and John Downey in the late 80s and early 90s,
is derived from the STEVIE by Tim Thompson and Tony Andrews
and currently lives at https://xvi.sourceforge.net

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.51
- Rebuilt for Fedora
