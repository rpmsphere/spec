Name: fth
Summary: Forth Scripting
Version: 1.4.1
Release: 1
Group: Development/Languages
License: BSD
URL: http://fth.sourceforge.net/
Source0: https://netix.dl.sourceforge.net/project/fth/fth/%{version}/%{name}-%{version}.tar.bz2

%description
Fth is a BSD licensed free software package which includes the interpreter fth
and the extension library libfth. You can use Fth as a command line interpreter
like Awk, Perl, or Ruby, you can write standalone Forth scripts, you can use
the repl fth for interactive input or you can link libfth into an application
using Fth as extension language.

%prep
%setup -q
#sed -i 's|define HAVE_BN.*|define HAVE_BN 0|' ficl/ficllocal.h

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README NEWS COPYING AUTHORS HISTORY
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man3/lib%{name}.3.*
%{_datadir}/aclocal/%{name}.m4

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuild for Fedora
