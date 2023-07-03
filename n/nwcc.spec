Name:         nwcc
Summary:      Small C Compiler
URL:          https://nwcc.sourceforge.net/
Group:        Development/Compiler
License:      BSD
Version:      0.8.3
Release:      7.1
Source0:      https://sourceforge.net/projects/nwcc/files/nwcc/nwcc%20%{version}/%{name}_%{version}.tar.gz
BuildRequires:  nasm

%description
Nils Weller's C Compiler (nwcc) is a small and portable ISO C90
compiler with some GNU and C99 extensions. nwcc is not yet intended
for serious production use. Instead it is mainly of interest for
developers to check their sources against a minimalistic C compiler.

%prep
%setup -q -n %{name}_%{version}
sed -i -e 's|\$INSTALLDIR/bin|\$INSTALLDIR/../bin|' -e 's|\$INSTALLDIR/lib|\$INSTALLDIR|' install.sh

%build
./configure --installprefix=%{_libdir}
make -i

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
DESTDIR=$RPM_BUILD_ROOT make install
cd $RPM_BUILD_ROOT%{_bindir}
for i in *
do
ln -sf ../lib/nwcc/bin/$i $i
done

%files
%doc CREDITS COPYING README.first CROSSCOMP NEWS USAGE nwcc.conf.sample
%{_bindir}/*
%{_libdir}/*.o
%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Nov 27 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.3
- Rebuilt for Fedora
