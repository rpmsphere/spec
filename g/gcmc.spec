Name: gcmc
Version: 1.8.2
Release: 3.1
Summary: G-Code Meta Compiler
Group: Development/Tools
License: GPL
URL: https://www.vagrearg.org/content/gcmc
Source0: https://www.vagrearg.org/gcmc/%{name}-%{version}.tar.gz
BuildRequires: bison
BuildRequires: flex

%description
Gcmc is a front-end language for generating G-code, SVG and DXF for CNC mills,
lathes, laser cutters and other numerical controlled machines employing G-code,
SVG or DXF. The language is a context-free grammar created to overcome the
archaic format of G-code programming and aims to be more readable and
understandable. Gcmc makes extensive use of vector mathematics to support the
3D nature of CNC machining.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --datadir=%{_datadir} --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/gcmc
%{_mandir}/man1/gcmc.1*
%{_datadir}/gcmc/
%{_docdir}/%{name}

%changelog
* Mon Jun 05 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.2
- Rebuilt for Fedora
* Wed Nov 27 2013 Bertho Stultiens <gcmc@vagrearg.org> 1.4.1-1
- Initial specfile release
