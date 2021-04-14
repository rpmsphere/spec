%undefine _debugsource_packages

Summary:  A Lesstif-based graphical FTP client
Name:  xmftp
Version:  1.0.4
Release:  5.1
License:  GPL
Group:  Applications/Networking
Source:  ftp://sunsite.unc.edu/pub/Linux/system/network/file-transfer/xmftp-1.0.4.tar.gz
BuildRequires: motif-devel
BuildRequires: libXpm-devel

%description
xmftp is a graphical FTP client capable of recursive downloads
and FTP resume. This distribution of xmftp is linked against LessTif.

%prep
%setup -n %{name}
sed -i 's|(unsigned char)sin.sa.sa_data\[\(.\)\] = v\[\(.\)\];|sin.sa.sa_data[\1] = (unsigned char)v[\2];|' source/ftplib/ftplib.c
sed -i 's|-lX11|-lX11 -Wl,--allow-multiple-definition|' source/Makefile

%build
make -C source

%install
install -Dm755 source/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc BUGS CHANGES FAQ
%{_bindir}/%{name}

%changelog
* Tue Jun 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
* Wed Nov 25 1998 David Jao <djao@dominia.mit.edu>
- Initial package
