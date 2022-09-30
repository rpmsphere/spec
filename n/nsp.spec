Summary:	A GPL Scientific Software Package
Name:		nsp
Version:	1.4cvs
Release:	1
License:	GPL and Specific for some included contribs (Scilab license)
Group:		Applications/Engineering
URL:		http://cermics.enpc.fr/~jpc/nsp-tiddly/mine.html
#Source:		http://cermics.enpc.fr/~jpc/nsp-tiddly/files/%{name}-%{version}.tgz
Source:		http://cermics.enpc.fr/~jpc/nsp-tiddly/files/nsp-cvs.tgz
BuildRequires:  atlas, automake
BuildRequires:  blas-devel, lapack-devel, libsndfile-devel, gtkglext-devel, fftw-devel, portaudio-devel, readline-devel, suitesparse-devel
BuildRequires:  gtksourceview3-devel, glpk-devel, libtirpc-devel, vte291-devel
BuildRequires:  webkitgtk4-devel, graphviz-devel, ocaml-num-devel
Obsoletes:      tumbi nsp2

%description
* It is based on a complete new rewrite of ScilabGtk.
* The interpreter is written in C and objects with an internal class system.
* Gtk toolkit can be used from Nsp through a set of generared wrappers. The language bindings and class for Nsp are generated, the generator being based on the pygtk generator for python.
* It is modular (modular interpreter design, possible dynamic link of internal and external libraries).
* It should compile on Linux, MacOSX-X11-Fink, Windows-Cygwin, Windows-Mingwin native Win32.
* A source version is available under CVS. Archive tarball, Fedora rpms, Debian package and win32 installer are also provided see this page
* It is a GPL software.

%prep
%setup -q -n %{name}
#sed -i 's|#define DOUBLE_ONLY|#undef DOUBLE_ONLY|' src/zcalelm/merge-sort.c
sed -i 's|$(CFLOPTS)|$(CFLOPTS) -I/usr/include/tirpc -ltirpc -Wl,--allow-multiple-definition -fPIE|' pvm3/Makefile* pvm3/*/Makefile*
sed -i 's|$(ARCHLIB)|$(ARCHLIB) -ltirpc -Wl,--allow-multiple-definition|' pvm3/Makefile* pvm3/*/Makefile*
sed -i 's|^LIBS=|LIBS=-Wl,--allow-multiple-definition |' config/Makefile.linux*
sed -i 's|fftw3 |fftw3 libtirpc |' Makefile*
sed -i 's|, KIND(t)||' src/lapack/zhpadm.f src/lapack/zgpadm.f
sed -i -e '165i let ss = Bytes.of_string s in' -e '165s| s | ss |' toolboxes/compilers/modelicac/src/optimization.ml
sed -i '38,39s|Pervasives|Stdlib|' toolboxes/compilers/paksazi/src/paksazi.ml
sed -i 's|Pervasives|Stdlib|' toolboxes/simport/release/src/slx_file_format/parsing/ocaml-xml/src/basics/*.ml* toolboxes/simport/release/src/slx_file_format/parsing/ocaml-xml/src/xml/parsing/xml_to_ast.ml toolboxes/simport/release/src/slx_file_format/parsing/ocaml-xml/src/xml/expand/xml_env.ml
#cp -f /usr/lib/rpm/redhat/config.* .
#cp -f /usr/share/automake-*/config.* /usr/share/automake-*/compile /usr/share/automake-*/missing .

%build
#export OCAMLPARAM="safe-string=1,_" CFLAGS="-g -O2 -Wl,--allow-multiple-definition"
export OCAMLPARAM="safe-string=1,_" CFLAGS="-g -O2 -Wl,--allow-multiple-definition -fPIE"
autoreconf -ifv ||:
#./autogen.sh --prefix=/usr
#make clean
./configure --prefix=/usr
make all

%install
rm -rf $RPM_BUILD_ROOT
make install-packaging prefix=$RPM_BUILD_ROOT%{_prefix} DESTDIR=%{buildroot}%{_libdir}/nsp
sed -i 's|/usr/lib|%{_libdir}|' config/nsp.desktop
install -Dm644 config/nsp.desktop $RPM_BUILD_ROOT%{_datadir}/applications/nsp.desktop
mkdir $RPM_BUILD_ROOT%{_prefix}/bin
ln -s ../%{_lib}/nsp/bin/nsp $RPM_BUILD_ROOT%{_bindir}/nsp
ln -s ../%{_lib}/nsp/bin/nsplibtool $RPM_BUILD_ROOT%{_bindir}/nsplibtool

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog COPYING
%{_bindir}/nsp*
%{_libdir}/nsp
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4cvs
- Rebuilt for Fedora
* Wed Oct 24 2012 Jean-Philippe Chancelier
- Package
