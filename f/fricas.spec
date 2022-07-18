%global lisp "sbcl"
%if %{lisp} == "sbcl" || %{lisp} == "clisp"
%global __os_install_post %{_rpmconfigdir}/brp-compress
%endif

Name:           fricas
Version:        1.3.8
Release:        1
Summary:        An advanced computer algebra system
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://%{name}.github.io/
#Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
Source0:	https://versaweb.dl.sourceforge.net/project/fricas/fricas/1.3.8/fricas-1.3.8-full.tar.bz2
BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  gnuplot
BuildRequires:  pkgconfig
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-pdftex
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  tex(breqn.sty)
BuildRequires:  tex(epsf.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(listings.sty)
BuildRequires:  tex(mleftright.sty)
BuildRequires:  tex(tensor.sty)
Requires:       emacs
Requires:       gnuplot
%if %{lisp} == "sbcl"
BuildRequires:  sbcl
Requires:       sbcl
%endif
%if %{lisp} == "clisp"
BuildRequires:  clisp
Requires:       clisp
%endif
%if %{lisp} == "ecl"
BuildRequires:  ecl
BuildRequires:  ecl-devel
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(libffi)
Requires:       ecl
%endif

%description
FriCAS is an advanced computer algebra system. Its capabilities range from
calculus (integration and differentiation) to abstract algebra. It can plot
functions and has integrated help system.

%package doc
Summary:        PDF documentation for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains the documentation for %{name} in PDF format.

%prep
%setup -q
sed -i -e '/\\usepackage{hyperref}/ a \ \
\\usepackage[svgnames]{xcolor}\
\\definecolor{linkcolor}{named}{DodgerBlue}\
\\hypersetup{dvips,colorlinks,linkcolor=linkcolor}' \
	src/doc/%{name}.sty

sed -i -e 's/xvfb-run -a -n 0/xvfb-run -a/' configure.ac
autoreconf

%build
%if "%{_arch}" == "i386"
%define dss 2048
%else
%define dss 4096
%endif

%if %{lisp} == "ecl"
%configure --with-lisp=%{lisp} --with-x
%endif
%if %{lisp} == "sbcl"
%configure --with-lisp=%{lisp}' --dynamic-space-size %{dss}' --with-x --with-gmp
%endif
%if %{lisp} == "clisp"
%configure --with-lisp=%{lisp} --with-x
%endif

%make_build -j1 MAYBE_VIEWPORTS=viewports
#%make_build -j1 -C src/doc book.pdf

%install
%make_install

%if %{lisp} == "sbcl"
sed -i -e '1 a export SBCL_HOME=%{_libexecdir}/sbcl' %{buildroot}%{_bindir}/%{name}
%endif

install -dm0755 %{buildroot}%{_mandir}/man1
install -m0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/e%{name}.1

install -dm0755 %{buildroot}%{_defaultdocdir}/%{name}
#install -m0644 src/doc/book.pdf %{buildroot}%{_defaultdocdir}/%{name}

%files
%license license/LICENSE.AXIOM src/etc/copyright
%doc ChangeLog README.rst
%{_libdir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*

#%files doc
#%{_defaultdocdir}/%{name}/*.pdf

%changelog
* Sun Jun 19 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.8
- Rebuilt for Fedora
* Mon Jul  5 2021 Anton Shvetz <shvetz.anton@gmail.com>
- The xvfb-run program is required when building PDF documentation
* Sat Jul  3 2021 Anton Shvetz <shvetz.anton@gmail.com>
- Update to v1.3.7
- Build PDF documentation from sources
* Sun Jun  6 2021 Anton Shvetz <shvetz.anton@gmail.com>
- Disable stripping of binaries when configured --with-lisp=sbcl
- Add runtime dependency on sbcl
* Sun Mar  8 2020 Anton Shvetz <tz@sectorb.msk.ru>
- Update to v1.3.6
* Sun Feb  3 2019 Anton Shvetz <tz@sectorb.msk.ru>
- Update to v1.3.5
* Fri Jul 13 2018 Anton Shvetz <tz@sectorb.msk.ru>
- Update to v1.3.4
* Mon Jun 18 2018 Anton Shvetz <tz@sectorb.msk.ru>
- Initial commit with v1.3.3
