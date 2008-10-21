Name:			fotoxx
Version:		5.4.1
Release:		%mkrel 1
Summary:		Fotoxx is an editor of image files from a digital camera
License:		GPLv2
Group:			Graphics
Source:			%name-%version.tar.gz
URL:			http://kornelix.squarespace.com/
BuildRoot:		%_tmppath/%name-%version-%release-buildroot
BuildRequires:		libgtk+2.0-devel
Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils

%description
Edit image files from a digital camera. Includes color
and contrast enhancement, red-eye removal, sharpen, 
crop, rotate, noise removal, HDR (high dynamic range) 
and panorama image compositing, thumbnail image browser, 
tag editing and search.

%prep
rm -rf %buildroot
%setup -q -n %name

# fix PREFIX in Makefile
sed -i -e "12 s:/usr/local:%buildroot%_exec_prefix:g" Makefile

%build
%make

%install
%makeinstall

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

