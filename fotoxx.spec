Name:			fotoxx
Version:		10.8.3
Release:		%mkrel 1
Summary:		Editor of image files from digital cameras
License:		GPLv3
Group:			Graphics
Source:			http://kornelix.squarespace.com/storage/downloads/%{name}-%{version}.tar.gz
Patch0:			fotoxx-10.2-link.patch
URL:			http://kornelix.squarespace.com/fotoxx/
BuildRoot:		%_tmppath/%name-%version-%release-buildroot
BuildRequires:		libgtk+2.0-devel
BuildRequires:		ufraw
BuildRequires:		perl-Image-ExifTool
BuildRequires:		tiff-devel
Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils
Requires:		exiv2
Requires:		ufraw
Requires:		perl-Image-ExifTool

%description
Edit image files from a digital camera. Includes color and contrast
enhancement, red-eye removal, sharpen, crop, rotate, noise removal,
HDR (high dynamic range) and panorama image compositing, thumbnail
image browser, tag editing and search.

%prep
%setup -q
%patch0 -p0

%build
%make PREFIX=%{_prefix} CXXFLAGS="%optflags" LDFLAGS="%ldflags"

%install
rm -rf %buildroot
%__make PREFIX=%{buildroot}%{_prefix} install

# man page
%__make PREFIX=%{buildroot}%{_prefix} manpage

# menu icon
mkdir -p %buildroot%_datadir/icons/hicolor/48x48/apps
cp %buildroot%_datadir/%name/icons/%name.png %buildroot%_datadir/icons/hicolor/48x48/apps/%name.png

# menu entry
mkdir -p %buildroot%_datadir/applications
cat << EOF > %buildroot%_datadir/applications/%name.desktop
[Desktop Entry]
Name=%name
GenericName=Image Editor
Comment=Edit image files from a digital camera
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;X-MandrivaLinux-CrossDesktop;
EOF

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_desktop_database
%update_icon_cache hicolor
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_desktop_database
%clean_icon_cache hicolor
%clean_menus
%endif

%files
%defattr(-,root,root,-)
%_docdir/%name
%_bindir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/48x48/apps/%name.png
%{_mandir}/man1/fotoxx.1*

