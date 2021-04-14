Name: qavimator
Summary: A tool to create animations for Second Life(TM)
Version: 0.272
Release: 7.1
License: GPL
Group: Applications/Multimedia/Animations
Source: %{name}-%{version}.tar.bz2
URL: http://qavimator.sf.net
BuildRequires: qt4-devel freeglut-devel cmake
BuildRequires: gcc-c++ libstdc++-devel libXmu-devel

%description
QAvimator is a Qt port of Vince Invincible's avimator, a bvh animation editor,
created for use in the 3D metaverse Second Life. The project is still in early
alpha stage and may or may not work on your system.

%prep
%setup -q

%build
#export CC=/usr/bin/gcc-4.3
#export CXX=/usr/bin/g++-4.3
CFLAGS="$RPM_OPT_FLAGS -Wno-format-security" CXXFLAGS="$RPM_OPT_FLAGS -Wno-format-security" \
cmake ${PWD} -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/%{_prefix} -DINSTALL_BIN=$RPM_BUILD_ROOT/%{_prefix}/bin -DINSTALL_DATA=$RPM_BUILD_ROOT/%{_prefix}/share/qavimator -DINSTALL_DATA_PATH=%{_prefix}/share/qavimator -DPREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
make install

cd $RPM_BUILD_ROOT

find . -type d -print|egrep -v "usr/bin$|usr/share$" > $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
%doc documentation/*

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.272
- Rebuilt for Fedora
* Fri Apr 25 2008 admin@eregion.de
- initial package
