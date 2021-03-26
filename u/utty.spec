Name: utty
Summary: KMS and CUSE based userspace /dev/tty?? device implementation
Version: 1.0
Release: 12.1
Group: System Environment/Daemons
License: unkonwn
URL: https://github.com/microcai/utty
Source0: %{name}-master.zip
BuildRequires: SDL-devel
BuildRequires: fuse-devel
BuildRequires: glib2-devel

%description
We implement VT in userspace daemon called uttyd, then PID 1 can swapon agetty
to use /dev/uttyXX. uttyd then use SDL to draw directly to framebuffer or to
an system compositor.

%prep
%setup -q -n %{name}-master
sed -i 's|2\.69|2.68|g' configure.ac

%build
aclocal
automake --add-missing
autoconf
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING NEWS README README.zh TODO
%{_bindir}/%{name}

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
