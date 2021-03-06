 i m p o r t   l o g g i n g 
 i m p o r t   t i m e 
 
 f r o m   .   i m p o r t   u t i l i t i e s 
 
 l o g   =   l o g g i n g . g e t L o g g e r ( _ _ n a m e _ _ ) 
 
 #   T h i s   f i l e   h a d   t o   b e   r e n a m e d   d u e   t o   " r o u n d ( ) "   a l r e a d y   b e i n g   a   f u n c t i o n 
 
 c l a s s   R o u n d : 
 	 d e f   _ _ i n i t _ _ ( s e l f ,   g a m e ,   t e a m ) : 
 	 	 " " "   R o u n d   o b j e c t   t h a t   s t o r e s   i n f o r m a t i o n   a b o u t   a   r o u n d ,   s u c h   a s   t e a m s , 
 	 	 w o r d s ,   a n d   s c o r e 
 
 	 	 : p a r a m   g a m e :   g a m e   t h e   r o u n d   i s   p a r t   o f 
 	 	 : p a r a m   t e a m :   t h e   t e a m   t h a t   i s   p l a y i n g   t o g e t h e r 
 	 	 " " " 
 	 	 s e l f . t e a m   =   t e a m 
 	 	 s e l f . g a m e   =   g a m e 
 	 	 s e l f . w o r d s   =   [ ] 
 	 	 s e l f . f i n i s h e d   =   F a l s e 
 	 	 s e l f . q u e s t i o n e r   =   N o n e 
 	 	 s e l f . a n s w e r e r   =   N o n e 
 
 	 @ p r o p e r t y 
 	 d e f   s c o r e ( s e l f ) : 
 	 	 " " "   T h e   c u r r e n t   s c o r e   " " " 
 	 	 s c o r e   =   0 
 	 	 f o r   w o r d   i n   s e l f . w o r d s : 
 	 	 	 s c o r e   + =   1   i f   w o r d [ ' s c o r e d ' ]   e l s e   0 
 	 	 r e t u r n   s c o r e 
 
 	 @ p r o p e r t y 
 	 d e f   i s _ f i n i s h e d ( s e l f ) : 
 	 	 " " "   W h e t h e r   o r   n o t   t h e   g a m e   i s   f i n i s h e d   " " " 
 	 	 r e t u r n   s e l f . s c o r e   = =   5 
 
 	 d e f   g e n e r a t e _ w o r d s ( s e l f ) : 
 	 	 w o r d s   =   [ ] 
 	 	 
 	 	 i f   l e n ( s e l f . g a m e . c u s t o m _ w o r d s )   >   0 : 
 	 	 	 
 	 
 	 a s y n c   d e f   s t a r t ( s e l f ) : 
 	 	 " " "   S t a r t   t h e   r o u n d   " " " 
 	 	 s e l f . q u e s t i o n e r ,   s e l f . a n s w e r e r   =   t u p l e ( s e l f . t e a m ) 
 	 	 s e l f . w o r d s   =   [ { 
 	 	 	 ' w o r d ' :   u t i l i t i e s . g e t _ r a n d o m _ w o r d ( ) , 
 	 	 	 ' s c o r e d ' :   F a l s e 
 	 	 }   f o r   _   i n   r a n g e ( 5 ) ] 
 
 	 	 a w a i t   s e l f . g a m e . g r o u p . s e n d ( 1 ,   ' R O U N D _ S T A R T ' ,   { 
 	 	 	 ' q u e s t i o n e r ' :   s e l f . q u e s t i o n e r . a s _ s a f e _ d i c t ( ) , 
 	 	 	 ' a n s w e r e r ' :   s e l f . a n s w e r e r . a s _ s a f e _ d i c t ( ) , 
 	 	 	 ' r o u n d ' :   l e n ( s e l f . g a m e . r o u n d s ) 
 	 	 } ) 
 
 	 	 a w a i t   s e l f . q u e s t i o n e r . s e n d ( 1 ,   ' Q U E S T I O N E R _ S T A R T ' ,   { 
 	 	 	 ' w o r d s ' :   s e l f . w o r d s 
 	 	 } ) 
 
 	 	 a w a i t   s e l f . a n s w e r e r . s e n d ( 1 ,   ' A N S W E R E R _ S T A R T ' ) 
 
 	 a s y n c   d e f   e n d ( s e l f ) : 
 	 	 " " "   E n d   t h e   r o u n d   " " " 
 	 	 s e l f . f i n i s h e d   =   T r u e 
 	 	 s e l f . g a m e . n e x t _ a c t i o n   =   i n t ( t i m e . t i m e ( ) )   +   1 0 
 
 	 	 a w a i t   s e l f . g a m e . g r o u p . s e n d ( 1 ,   ' R O U N D _ E N D ' ,   { 
 	 	 	 ' w o r d s ' :   s e l f . w o r d s , 
 	 	 	 ' c o o l d o w n ' :   1 0 
 	 	 } ) 
 
 	 a s y n c   d e f   a n s w e r ( s e l f ,   w o r d ) : 
 	 	 " " "   T r y   t o   g u e s s   a   w o r d   f o r   t h e   r o u n d 
 
 	 	 : p a r a m   w o r d :   t h e   w o r d   t o   g u e s s 
 	 	 " " " 
 	 	 f o r   i n d e x ,   w o r d _ d a t a   i n   e n u m e r a t e ( s e l f . w o r d s ) : 
 	 	 	 i f   w o r d _ d a t a   ! =   w o r d : 
 	 	 	 	 c o n t i n u e 
 
 	 	 	 w o r d _ d a t a [ ' s c o r e d ' ]   =   T r u e 
 	 	 	 a w a i t   s e l f . g a m e . g r o u p . s e n d ( 1 ,   ' C O R R E C T _ W O R D ' ,   { 
 	 	 	 	 ' w o r d ' :   w o r d , 
 	 	 	 	 ' i n d e x ' :   i n d e x 
 	 	 	 } ) 
 
 	 	 i f   s e l f . i s _ f i n i s h e d : 
 	 	 	 a w a i t   s e l f . e n d ( ) 
