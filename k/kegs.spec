Name:         kegs
License:      COPYRIGHT
Group:        Emulators
Version:      0.91
Release:      4.1
Summary:      Apple IIgs emulator
Source:       %name.%version.tar.gz
Patch0:       %name.%version.dif
BuildRequires: libX11-devel, libXext-devel

%description
Requires ROM and disk images to work.

%prep
%setup -q -n %name.%version
%patch0 -p0

%build
# build section
cd src
rm -f vars
cat <<EOT >vars
TARGET = xkegs
OBJECTS = \$(OBJECTS1) xdriver.o
CCOPTS = $RPM_OPT_FLAGS
%ifarch %ix86 x86_64 %arm ia64
OPTS = -DKEGS_LITTLE_ENDIAN -DNDEBUG
%else
OPTS = -DNDEBUG
%endif
SUFFIX =
NAME = xkegs
LDFLAGS =
LDOPTS =
LD = \$(CC)
EXTRA_LIBS = -lXext
EXTRA_SPECIALS =

AS = cc
PERL = perl

XOPTS =
EOT

make %{?jobs:-j%jobs}

%install
# install section
install -D -m 755 xkegs $RPM_BUILD_ROOT/%{_bindir}/xkegs
install -D -m 644 config.kegs $RPM_BUILD_ROOT/%{_datadir}/%{name}/config.kegs
chmod 755 $RPM_BUILD_ROOT%{_bindir}/xkegs

%files
# %{_docdir}/%{name}/*.txt
# %{_bindir}/kegs
%{_bindir}/xkegs
%{_datadir}/%{name}/config.kegs
# %{_sysconfdir}/default.config.kegs

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.91
- Rebuilt for Fedora
* Mon Oct 24 2011 Zombie Ryushu <ryushu@mandriva.org> 0.91-2mdv2012.0
+ Revision: 706125
- Fix kegs overwriting itself with a blank file
- Backport for 2011 and 2010.2
* Sun Oct 23 2011 Zombie Ryushu <ryushu@mandriva.org> 0.91-1
+ Revision: 705792
- imported package kegs
