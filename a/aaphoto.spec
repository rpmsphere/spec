Name:		aaphoto		
Version:	0.43
Release:	10.1
Summary:	Automatic color correction of photos
Group:		Applications/Multimedia		
License:	GPLv3+	
URL:		http://log69.com/aaphoto_en.html		
Source0:	https://github.com/log69/%{name}/archive/v%{version}.tar.gz
BuildRequires:	jasper-devel, libpng-devel

%description
Auto Adjust Photo is a tiny command-line image manipulation 
tool for automatic color correction of photos. It tries to 
make the picture look better. The  program does this by analyzing 
the input image and then sets the most optimal contrast, gamma, 
color balance and saturation for it.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING COPYRIGHT LICENSE NEWS README TODO
%{_bindir}/%{name}

%changelog
* Wed May 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.43
- Rebuilt for Fedora
* Tue Oct 01 2013 Simone Sclavi <darkhado@gmail.com> 0.43-1
- Update to 0.43 release
* Sat Sep 28 2013 Simone Sclavi <darkhado@gmail.com> 0.42-1
- Update to 0.42 release
* Sat Jun 8 2013 Simone Sclavi <darkhado@gmail.com> 0.41-1
- Initial build
