%undefine _missing_build_ids_terminate_build

Name: scicoslab
Version: 4.4.1
Release: 65.1
License: Scilab License
URL: http://www.scicoslab.org
BuildRequires: gcc-gfortran, libXt-devel
BuildRequires: tcl-devel, tk-devel, vte-devel, readline-devel
Group: Applications/Engineering
Summary: A scientific software package for numerical computations
Source: http://cermics.enpc.fr/~jpc/scilab-gtk-tiddly/files/%{name}-%{version}.tgz
BuildRequires: webkitgtk-devel
BuildRequires: libtirpc-devel
Obsoletes: scilabgtk

%description
ScicosLab is the new name of ScilabGtk. This change of name has been
decided in order to avoid all confusion with Scilab, which is no longer
developed at INRIA.

%prep
%setup -q -n %{name}
sed -i '1s|sh5|sh|' bin/dold
sed -i 's|$(CFLOPTS)|$(CFLOPTS) -I/usr/include/tirpc -ltirpc|' pvm3/*/Makefile.aimk
sed -i 's|pkg-config vte|pkg-config vte libtirpc|' configure*
sed -i 's|INCLUDES=|INCLUDES=-I/usr/include/tirpc |' Makefile.incl.mak

%build
export LDFLAGS="-Wl,--allow-multiple-definition -lgthread-2.0 -ltirpc"
./autogen.sh --prefix=%{buildroot}/usr
sed -i 's|-I/usr/include|-I/usr/include -I/usr/include/tirpc|' Makefile.incl
make all

%install
make install

%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
rm -rf %{buildroot}%{_libdir}/scicoslab-svn/contrib/cs5

pushd %{buildroot}%{_bindir}
rm scilab
ln -fs %{_libdir}/scicoslab-svn/bin/scilab %{name}
rm intersci-n
ln -fs %{_libdir}/scicoslab-svn/bin/intersci-n intersci-n
rm intersci
ln -fs %{_libdir}/scicoslab-svn/bin/intersci intersci
popd

pushd $RPM_BUILD_ROOT%{_libdir}/scicoslab-svn
sed -i 's|%{buildroot}||' bin/scilab config/configuration Path.incl bin/BEpsf bin/Blatexprs bin/Blatexpr bin/Blpr bin/Blatexpr2 Makefile util/Blatdoc util/Blatdocs
chmod +x bin/*
popd

install -Dm644 config/fedora-scilab-gtk.desktop %{buildroot}%{_datadir}/applications/scicoslab.desktop
sed -i -e 's|-gtk|-svn|' -e 's|Development;||' -e 's|/usr/lib|%{_libdir}|' %{buildroot}%{_datadir}/applications/scicoslab.desktop

%clean 
rpm -fr $RPM_BUILD_ROOT

%files
%doc ACKNOWLEDGEMENTS README* CHANGES
%{_bindir}/*
%{_datadir}/*
%{_libdir}/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 02 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.4.1
- Rebuilt for Fedora
* Mon Apr 09 2012 Jean-Philippe Chancelier
- Package
